from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.validators import UniqueValidator
from user.utils import send_mail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields =('username','email','id')
class UserRegisterSerializer(serializers.ModelSerializer):
    gender_choices = (
    ("M","Male"),
    ("F","Female"),
    ("O","Other")
)
    email = serializers.EmailField(
        required = True,
        validators=[UniqueValidator(queryset=User.objects.all())]#so that one email has only one userid
    )
    password = serializers.CharField(write_only = True,required = True) #write_only so that it will not be send as query for security purpose
   
    dob = serializers.DateTimeField()
    country = serializers.CharField(max_length = 80)
    city = serializers.CharField(max_length = 150)
    gender = serializers.ChoiceField(choices=gender_choices)
    interest = serializers.CharField()
    

    class Meta:
        model = User
        fields = ('username','password','email','dob','country','city','gender','interest')
        extra_kwargs={
      'password':{'write_only':True}
    }   
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            # confirm_password = validated_data['confirm_pssword'],
            dob = validated_data['dob'],
            country = validated_data['country'],
            city = validated_data['city'],
            gender = validated_data['gender'],
            interest = validated_data['interest']
        )
        print(user)
        return user 

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False)

class ChangePasswordSeriaizer(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    # password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta :
        fields = ['password']

    def validate(self,data):
        password = data.get('password')
        user = self.context.get('user')
       
        user.set_password(password)
        user.save()
        return data

class PasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length =255)

    class Meta:
        field =['email']
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            id = user.id
            uid = urlsafe_base64_encode(force_bytes(id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token
            print(link)
            subject ='This mail is for resetting password'
            body = 'Click the link to change the password : '+link
            data={
                'subject':subject,
                'body': body,
                'to' : user.email
            }
            send_mail(data)
            return attrs
        else:
            raise serializers.ValidationError("This email is not registerd")    


class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    class Meta:
        fields = ['password']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            id = smart_str(urlsafe_base64_decode(self.context.get('uid')))
            user = User.objects.get(id = id)
            token = self.context.get('token')
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError("token not valid or Expired")
            
            user.set_password(password)
            user.save()
            return attrs
        except ValueError:
            raise serializers.ValidationError("Value error UID not valid")

