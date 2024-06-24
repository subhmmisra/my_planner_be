from rest_framework import serializers
from apps.users import services as user_services
from apps.users.models import UserManager, User


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, required=True)
    password = serializers.CharField(required=True)

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        user = user_services.get_user_by_email(email=value)
        if not user:
            raise serializers.ValidationError("User does not exist")
        return value


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if "password" and "confirm_password" in attrs:
            confirm_password = attrs.pop("confirm_password")
            if attrs["password"] != confirm_password:
                raise serializers.ValidationError("Passwords do not match.")
            return attrs
        raise serializers.ValidationError("Passwords do not match.")
