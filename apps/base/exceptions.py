from django.core.exceptions import PermissionDenied as DjangoPermissionDenied
from django.http import Http404
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, status
from rest_framework.response import Response


class BaseException(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Unexpected error")

    def __init__(self, detail=None):
        self.detail = detail or self.default_detail


class NotFound(BaseException, Http404):
    """Exception used for not found objects.
    """

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _("Not found.")


class BadRequest(BaseException):
    """Exception used on bad arguments detected on api view.
    """

    default_detail = _("Wrong arguments.")


class WrongArguments(BadRequest):
    """Exception used on bad arguments detected on service. This is same as `BadRequest`.
    """

    default_detail = _("Wrong arguments.")