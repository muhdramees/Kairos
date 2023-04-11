from django.conf import settings
from twilio.rest import Client
import random
 

class MessageHandler:
    otp =  None
    
    def _init_(self,phone_number,otp) -> None:
        self.phone_number = phone_number
        self.otp = otp
        print("generated otp",self.otp)


    def send_otp(self):
        account_sid=settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        client = Client(account_sid,auth_token)
        verification = client.verify \
                   .v2 \
                   .services('VA1e8771e5063b54d53dc20dce05e786ed') \
                   .verifications \
                   .create(to =f"+91{ self.phone_number}",channel = 'sms')

    def validate(self):
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        client = Client(account_sid,auth_token)
        verification_check = client.verify  \
           .v2 \
           .services('VA1e8771e5063b54d53dc20dce05e786ed') \
           .verification_checks \
           .create(to = f"+91{self.phone_number}",code = f"{self.otp}")

        validation = verification_check.status
        print(validation)
        return validation
    




# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client

# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "AC27d86433b01e6e540b272ac16f1d38af"
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]
# verify_sid = "VA1e8771e5063b54d53dc20dce05e786ed"
# verified_number = "+918089865321"

# client = Client(account_sid, auth_token)

# verification = client.verify.v2.services(verify_sid) \
#   .verifications \
#   .create(to=verified_number, channel="sms")
# print(verification.status)

# otp_code = input("Please enter the OTP:")

# verification_check = client.verify.v2.services(verify_sid) \
#   .verification_checks \
#   .create(to=verified_number, code=otp_code)
# print(verification_check.status)