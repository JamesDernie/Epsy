# Rest Framework
from rest_framework.exceptions import APIException


class NoUrlProvided(APIException):
    status_code = 400
    default_detail = 'No url has been provided'
    default_code = 'no_url_provided'
