#from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from apps.users.auth.apis import AuthViewSet
from apps.users.apis import UserViewset

default_router = DefaultRouter(trailing_slash=False)


default_router.register("auth", AuthViewSet, basename="auth")

urlpatterns = default_router.urls