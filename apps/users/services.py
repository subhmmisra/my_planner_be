# apps/users/services.py
from django.contrib.auth import get_user_model

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
import random
import string
from django.utils import timezone
from apps.users.models import UserForgotPasswordToken


from apps.base import exceptions as exc
from apps.users.models import User


def get_and_authenticate_user(phone_number, password):
    user = authenticate(username=phone_number, password=password)
    if user is None:
        raise exc.WrongArguments("Invalid username/password. Please try again!")
    return user


def create_user_account(phone_number, password=None, **kwargs):
    # TODO: Remove case conversions
    user_details = kwargs
    if password is not None:
        user_details["password"] = password
    user = get_user_model().objects.create_user(phone_number=phone_number, **user_details)
    return user


def get_user_by_email(email: str):
    user_email = User.objects.filter(email=email).first()
    user = user_email if user_email else None
    return user


def get_user_by_phone(phone_number: str):
    user_email = User.objects.filter(phone_number=phone_number).first()
    user = user_email if user_email else None
    return user


def create_password_token():
    random_string = "".join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return random_string


def set_password_token(user, token):
    if not user:
        return None
    UserForgotPasswordToken.objects.create(user=user, token=token)
    return True