
from django.urls import path
from . import views

urlpatterns = [
       path('', views.user_login , name="user_login"),
       path('user-registration/', views.user_registration , name="user_registration"),
       path('user-logout/', views.user_logout , name="user_logout"),
       path('otp-login/', views.otp_login , name="otp_login"),
       # path('send-sms/', views.send_sms , name="send_sms"),
       path('send-otp/', views.send_otp , name="send_otp"),
       path('verify-otp/', views.verify_otp , name="verify_otp"),
 
 
       
              
]