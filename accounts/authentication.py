from django.conf import settings
from rest_framework import authentication, exceptions
import jwt

from . import models


class CustomUserAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        else:
            token = request.COOKIES.get('jwt')

        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed('Unauthorized')

        user = models.User.objects.filter(id=payload['id']).first()

        return (user, None)