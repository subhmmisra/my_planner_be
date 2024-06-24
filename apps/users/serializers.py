from apps.users.models import User, UserManager
from rest_framework import serializers
from apps.users import services as user_services
import re


class RegisterBaseSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    address = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=True)

    class Meta:
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
            "phone_number",
            "address",
        ]
        model = User

    def validate_email(self, value):
        if value:
            user = user_services.get_user_by_email(email=value)
            if user:
                raise serializers.ValidationError("Email is already taken.")
            return UserManager.normalize_email(value)
    

    def validate(self, attrs):
        if "password" and "confirm_password" in attrs:
            confirm_password = attrs.pop("confirm_password")
            if attrs["password"] != confirm_password:
                raise serializers.ValidationError("Passwords do not match.")
            return attrs
    

    def validate_phone_number(self, value):
        if value:
            user = user_services.get_user_by_phone(phone_number=value)
            if user:
                raise serializers.ValidationError("Phone number already taken.")
            pattern = re.compile(r'^[6789]\d{9}$')
            if bool(pattern.match(value)):
                return value

class RegisterResponseSerializer(RegisterBaseSerializer):

    class Meta(RegisterBaseSerializer.Meta):
        fields = RegisterBaseSerializer.Meta.fields + ["full_name"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address",
        ]