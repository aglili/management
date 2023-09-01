from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist():
            raise serializers.ValidationError("User Does Not Exist",code=404)
        
        user = authenticate(username=username,password=password)

        if not user:
            raise serializers.ValidationError("Invalid Login Credentials")
        
        return attrs

    def generate_jwt_tokens(self,attrs):
        username = attrs.get("username")
        user = User.objects.get(username=username)
        refresh = RefreshToken.for_user(user=user)

        token_data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return token_data



        

        


