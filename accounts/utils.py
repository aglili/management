import pyotp
from trycourier import Courier
from dotenv import load_dotenv
import os

load_dotenv()

def generate_otp():
    otp_secret = pyotp.random_base32()
    totp = pyotp.TOTP(otp_secret,interval=300)
    return totp.now(), otp_secret

def send_email(email:str,otp_code):
    client = Courier(auth_token=os.getenv("COURIER_KEY"))

    client.send_message(
    message={
        "to": {
        "email": email,
        },
        "template": "GNB5W440P5MVDRKAVYTKPPSWSS4A",
        "data": {
        "otp_code": otp_code,
        },
    }
    )
