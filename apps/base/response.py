import rest_framework.response
from django import http


class Response(rest_framework.response.Response):
    """The various HTTP responses for use in returning proper HTTP codes.
    """

    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
    ):
        super().__init__(data, status, template_name, headers, exception, content_type)


class Ok(Response):
    """200 OK

    Should be used to indicate nonspecific success. Must not be used to
    communicate errors in the response body.
    In most cases, 200 is the code the client hopes to see. It indicates that
    the REST API successfully carried out whatever action the client requested,
    and that no more specific code in the 2xx series is appropriate. Unlike
    the 204 status code, a 200 response should include a response body.
    """

    status_code = 200


class Created(Response):
    """201 Created

    Must be used to indicate successful resource creation.
    A REST API responds with the 201 status code whenever a collection creates,
    or a store adds, a new resource at the client's request. There may also be
    times when a new resource is created as a result of some controller action,
    in which case 201 would also be an appropriate response.
    """

    status_code = 201
    

class NoContent(Response):
    """204 No Contents

    Should be used when the response body is intentionally empty.
    The 204 status code is usually sent out in response to a PUT, POST, or
    DELETE request, when the REST API declines to send back any status message
    or representation in the response message's body. An API may also send 204
    in conjunction with a GET request to indicate that the requested resource
    exists, but has no state representation to include in the body.
    """

    status_code = 204

class BadRequest(Response):
    """400 Bad Request

    May be used to indicate nonspecific failure.
    400 is the generic client-side error status, used when no other 4xx error
    code is appropriate.
    """

    status_code = 400