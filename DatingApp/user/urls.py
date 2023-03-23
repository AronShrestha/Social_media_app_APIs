from django.urls import path , re_path
from user import views
from .views import * 



urlpatterns =[
    path('',views.Home),
    path('register',views.RegisterUser),
    path('login',views.LoginIn.as_view(),name='login'),
    path('change-password',ChangePasswordView.as_view(),name='change-password'),
    path('password-reset-email',PasswordResetEmail.as_view(),name='password-reset-email'),
    path('password-reset/<uid>/<token>',PasswordReset.as_view(),name='password-resetl')
    # path('logout',views.Logout.as_view(),name='logout'),
    # path('logout',knox_views.LogoutView.as_view(),name='logout'),
    # path('register',UserRegister.as_view(),name = 'register'),
]