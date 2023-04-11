from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import EmailUser,Otp
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
   
    class Meta:
        model = EmailUser
        fields = ('first_name', 'last_name', 'email', 'phone_number')


class LoginForm(forms.Form):
    email = forms.CharField(label='Email',  required=True, widget=forms.EmailInput)
    password = forms.CharField(label='Password', max_length=255, required=True, widget=forms.PasswordInput())


class OtpLoginForm(forms.Form):

    phone_number = forms.CharField(max_length=13 )
    # otp = forms.IntegerField()
    

class EditUserForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = '__all__'