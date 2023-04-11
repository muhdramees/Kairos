from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, OtpLoginForm, EditUserForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from twilio.rest import Client
import string
import random
from django.contrib.auth.models import User
from random import randint
from django.conf import settings
from .models import EmailUser, Otp



# Your Account SID from twilio.com/console
account_sid = "AC27d86433b01e6e540b272ac16f1d38af"
# Your Auth Token from twilio.com/console
auth_token = "c45d09a66f986f502d0d96f0cf61509c"

client = Client('AC27d86433b01e6e540b272ac16f1d38af',
                'c45d09a66f986f502d0d96f0cf61509c')


# # Create your views here.
# ============================================================
# =================== Registration ===========================
# ============================================================


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_login')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})


# ============================================================
# ================= End Registration =========================
# ============================================================


# ============================================================
# ====================== Login ===============================
# ============================================================

def user_login(request):

    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            

            if user is not None:
                if user.blocked == False:
                    login(request, user)
                    messages.info(request, f"You are logged in Successfully")
                    return redirect('home')
                else:
                    messages.error(request, "Your Account is blocked")
                    
            else:
                messages.error(request, "Invalid email and password")

        else:
            messages.error(request, "Invalid email or password")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {'form': form})


# ============================================================
# =================== End Login ==============================
# ============================================================


# ============================================================
# =================== User Logout ============================
# ============================================================
@login_required
def user_logout(request):

    logout(request)

    return redirect('user_login')


# ============================================================
# =================== End Logout ==============================
# ============================================================


# def register_otp(request):

#     otp = generate_otp()

#     request.session['otp'] = otp


def otp_login(request):
    form = OtpLoginForm

    
    return render(request, 'account/otp-login.html', {'form': form})


# def generate_otp():
#     return ''.join(random.choices(string.digits, k=6))


# def send_sms(request):
#     phone_number = request.POST['phone_number']

#     message = client.messages.create(
#         to=phone_number,
#         from_="+19295216600",
#         body=generate_otp
#     )

#     return HttpResponse("OTP send to "+phone_number)


def send_otp(request):

    otp = randint(10000, 99999) 
    phone_number = request.POST.get('phone_number')


    Otp.objects.create(phone_number=phone_number, otp=otp)

    # client = Client('AC27d86433b01e6e540b272ac16f1d38af',
    #                 'c45d09a66f986f502d0d96f0cf61509c')
    # message = client.messages.create(
    #     body=f'Your OTP is {otp}',
    #     from_=+19295216600,
    #     to=phone_number
    # )

    account_sid = 'AC27d86433b01e6e540b272ac16f1d38af'


    auth_token = '[c45d09a66f986f502d0d96f0cf61509c]'
    client = Client('AC27d86433b01e6e540b272ac16f1d38af', 'c45d09a66f986f502d0d96f0cf61509c')

    message = client.messages.create(
        messaging_service_sid='MG3ae9e9bf9d6deaedf2989e61aba3d203',
        body=f'Your OTP is {otp}',
        to=phone_number
    )

    return render(request,"account/verify-otp.html")

def verify_otp(request):

    user_otp = request.POST.get('otp')
    phone_number = request.POST.get('phone_number')
    print("--------------------------------------------------------")
    print(user_otp)
    
    

    try:
        otp = Otp.objects.get(phone_number=phone_number)
        print("######################################################")
        print(otp.otp)

        if otp.otp == user_otp:

            return HttpResponse('OTP verified')

        else:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            return HttpResponse('Invalid OTP')

    except Otp.DoesNotExist:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return HttpResponse('Invalid OTP')



    # otp = Otp.objects.get(phone_number=phone_number)

    # if otp.otp == user_otp:

    #     return HttpResponse('OTP verified')

    # else:
    #     return HttpResponse("invalid OTP")
