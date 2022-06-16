from braces.views import CsrfExemptMixin
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterView(APIView, CsrfExemptMixin):
    '''
    - 사용자가 데이터를 입력해 회원가입을 진행합니다.
    '''
    authentication_classes = []

    def post(self, request):

        user = User.objects.create_user(
            username=request.data['id'],
            password=request.data['password'],
            email=request.data['email']
        )

        user.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})


class LoginView(APIView, CsrfExemptMixin):
    '''
    - 사용자가 입력한 데이터를 받아서 로그인을 합니다.
    '''
    authentication_classes = []

    def post(self, request):

        user = authenticate(
            username=request.data['id'],
            password=request.data['password']
        )

        if user is not None:
            token = Token.objects.get(user=user)
            email = User.objects.get(user=user).values_list('email')[0]
            return Response({"Token": token.key, "email": email})
        else:
            return Response(status=401)
