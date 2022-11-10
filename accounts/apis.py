from rest_framework import views, response, exceptions, permissions
from . import serializer as user_serializer
from . import services, authentication
from .models import User
import re


class RegisterApi(views.APIView):

    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.email
        username = serializer.validated_data.username

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, email):
            return response.Response({'message': 'invalid email'}, status=200)

        if ' ' in username.strip():
            return response.Response({'message': 'invalid username'}, status=200)

        if User.objects.filter(email=email).exists():
            return response.Response({'message': 'email already in use'}, status=200)

        if User.objects.filter(username=username).exists():
            return response.Response({'message': 'username already in use'}, status=200)

        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)

        return response.Response(data=serializer.data)


class LoginApi(views.APIView):

    def post(self, request):
        password = request.data['password']
        username = request.data['user'].lower()

        if '@' in username:
            user = services.user_email_selector(username)
        else:
            user = services.user_username_selector(username)

        if user is None:
            raise exceptions.AuthenticationFailed('Invalid Credentials')

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed('Invalid Credentials')

        token = services.create_token(user_id=user.id)

        resp = response.Response({'message': 'success'})
        resp.set_cookie(key='jwt', value=token, httponly=True)

        return resp


class UserApi(views.APIView):
    """
    This endpoint can only be used
    if the user is authenticated
    """

    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)


class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie('jwt')

        resp.data = {'message': "Volte sempre"}

        return resp


class EditApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def patch(self, request):
        user = User.objects.filter(id=request.user.id).first()

        if 'username' in request.data:
            checkUser = User.objects.filter(username=request.data['username'])
            if len(checkUser) > 0:
                if request.user.username != request.data['username']:
                    return response.Response({'message': 'Username already in use'})
            else:
                user.username = request.data['username']

        if 'email' in request.data:
            checkUser = User.objects.filter(email=request.data['email'])
            if len(checkUser) > 0:
                if request.user.username != request.data['email']:
                    return response.Response({'message': 'Email already in use'})
            else:
                user.email = request.data['email']

        if 'password' in request.data:
            if 'oldPassword' not in request.data or not user.check_password(request.data['oldPassword']):
                return response.Response({'message': 'Old password not match'})

            user.set_password(request.data['password'])

        if 'profilePic' in request.data:
            user.profilePic = request.data['profilePic']
        if 'name' in request.data:
            user.name = request.data['name']
        if 'birthdate' in request.data:
            user.birthdate = request.data['birthdate']

        user.save()
        serializer = user_serializer.EditSerializer(user)

        return response.Response(data=serializer.data, status=201)

    def put(self, request):
        return self.patch(request)


class CheckLogin(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return response.Response({'message': 'logged'}, 200)
