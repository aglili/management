from rest_framework.response import Response
from .serializers import SignUpSerializer,LoginSerializer,RequestPasswordResetSerializer,VerifyOTPSerilizer,ChangePasswordSerializer
from rest_framework.decorators import api_view
from .utils import generate_otp,send_email
from pyotp import TOTP
from .models import User




@api_view(["POST"])
def user_sign_up(request):
    try:
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {
                "status":True,
                "data":serializer.data
            }
        ,status=201)
    except Exception as e:
        return Response(
            {
                "status":False,
                "error": str(e)
            }
        ,status=400)
    

@api_view(["POST"])
def user_login(request):
    try:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            tokens = serializer.generate_jwt_tokens(serializer.validated_data)
        return Response(
            {
                "status":True,
                "tokens":tokens
            }
        ,status=200)
    except Exception as e:
        return Response(
            {
                "status":False,
                "error": str(e)
            }
        ,status=400)


@api_view(['POST'])
def request_password_reset(request):
    try:
        serializer = RequestPasswordResetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            otp,otp_secret=generate_otp()
            request.session["otp_secret"] = otp_secret
            send_email(email=serializer.validated_data["email"],otp_code=otp)
        return Response (
            {
                "status":True,
                "message": "OTP Sent"
            }
        ,status=200)
    except Exception as e:
        return Response(
            {
                "status":False,
                "error": str(e)
            }
        ,status=400)
    

@api_view(["POST"])
def verify_otp(request):
    try:
        serializer = VerifyOTPSerilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            otp = serializer.validated_data['otp']
            otp_secret = request.session['otp_secret']
            if not otp_secret:
                return Response(
                    {
                        "error": "Request OTP Again"
                    }, status=400
                )
            totp = TOTP(s=otp_secret, interval=300)
            if totp.verify(otp):
                return Response(
                    {
                        "status":True,
                        "message":"Verified"
                    }
                ,status=200)
            else:
                return Response(
                    {
                        "status":False,
                        "message":"Not Verified"
                    }
                ,status=400)
    except Exception as e:
        return Response(
            {
                "status":False,
                "error": str(e)
            }
        ,status=400)
    


        
@api_view(['PATCH'])
def change_password(request):
    try:
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            new_password = serializer.validated_data['new_password']
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            return Response(
                {
                    "status": True,
                    "message": "Password Has Been Reset"
                },
                status=200
            )
    except Exception as e:
        return Response(
            {
                "status": False,
                "error": str(e)
            },
            status=400
        )
    


    #

    

                





            

