from rest_framework.response import Response
from .serializers import SignUpSerializer,LoginSerializer
from rest_framework.decorators import api_view




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






