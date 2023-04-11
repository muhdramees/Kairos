def otp_validate(request):
    if request.method == 'POST' and request.POST['otpnumber']:
        print('ttttttttttttttttttttttttttt')
        otp1 = request.POST['otpnumber']
        print(otp1)
        phone_number = request.POST['phone_number']
        user_name=request.POST['user_name']
        user_email=request.POST.get('user_email')
        password=request.POST.get('password')
        validate=MessageHandler(phone_number,otp1).validate()
        print(validate,'jjjjjjjjjjjjjjjjjjjjj')

        if validate == 'approved':
            print('oooooooooooooooooo')
            user=Account.objects.create_user(username=user_name,email=user_email,password=password,phone_number=phone_number)
            user.save() 
            messages.info(request,"Account Created")
            print('user reated')
            return redirect('homepage')
        else:
            messages.info(request,'Wrong OTP')
            context={

                'phone_number':phone_number,
                'user_email':user_email,
                'user_name':user_name,
                'password': password

            }
            return render(request,'otp.html',context)
    return render(request,'otp.html')