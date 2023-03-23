# from passlib.context  import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# def hash(password: str):
#     return pwd_context.hash(password)


# def verify(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

from django.core.mail import EmailMessage
import os

def send_mail(data):
    email = EmailMessage(
        subject= data['subject'],
        body = data['body'],
        from_email = os.environ.get('FROM'),
        
        to = [data['to']]

        )
    print("Email from "+os.environ.get('FROM'))
    
    
    email.send()
