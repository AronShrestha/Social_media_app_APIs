from django.shortcuts import render
from .serializers import UserRegisterSerializer,LoginSerializer,ChangePasswordSeriaizer,PasswordResetEmailSerializer,PasswordResetSerializer
from rest_framework.response import Response
# from rest_framework import generics,permissions,viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
# from knox.views import LoginView as KnoxLoginView
# from knox.views import LogoutView as knoxLogoutView
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from user.error import CustomizeRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


#for generating tokens
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    } 

def Home(request):
    print("Printing request data")
    print(request.body)
    print(request.method)
   
    print(request.content_params)
    return HttpResponse("hello")

# class UserRegister(generics.GenericAPIView):
#     serializer_class = UserRegisterSerializer
#     def post(self,request,*args,**kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception = True)
#         user = serializer.save()
#         return Response(UserRegisterSerializer(user).data)    
#     def get(self,request):
#         return HttpResponse("hello")

@api_view(['GET','POST'])
def RegisterUser(request):
    if request.method == "POST":
        print("Printing request data")
        print(request.body)
        print(request.data)
        print(request.method)
        print(request.META)   
        print(request.content_params)
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':"Registration Successful"},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    if request.method == "GET":
        return HttpResponse("hello")
    
class LoginIn(APIView): 
    renderer_classes = [CustomizeRenderer]
    
    def post(self, request):    
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            # login(request,user)
            return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

# class Logout(knoxLogoutView):
#     permission_classes =(permissions.AllowAny,)
#     def post(self,request):
#         print("We are logging out **********************************")
#         return super(Logout,self).post(request)

class ChangePasswordView(APIView):
    render_classes =[CustomizeRenderer]
    permission_classes = [IsAuthenticated] #user resetting password when he is already logged in
    def post(self,request):
        serializer = ChangePasswordSeriaizer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password changed Successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#If we had only searilize in serializers we could implement change password as below
        #     if serializer.is_valid(raise_exception=True):
        #     password = serializer.data.get('password')
        #     request.user.set_password(password)
        #     # print("password"+password)
        #     request.user.save()
        #     return Response({'msg':'Password changed Successfully'},status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PasswordResetEmail(APIView):
    """
   
    Sending email for Reseting password when user is not already logged in 
    """
    renderer_classes = [CustomizeRenderer]
    def post(self,request):
        serializer = PasswordResetEmailSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
         return Response({'msg':'Password Reset Email Sent'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordReset(APIView):
    """
    Reseting password when user is not already logged in via link
    """
    renderer_classes = [CustomizeRenderer]
    def post(self,request,uid,token):
        serializer =  PasswordResetSerializer(data = request.data,
        context = {
            'uid':uid,
            'token':token,
        }
        )
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Done'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



