from django.contrib.auth import authenticate

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


from utils.response_handling import ErrorResponse, SuccessResponse

from .models import DjangoUser

from .serializers import DjangUserChangePasswordEmailWiseSerializer, DjangUserChangePasswordSerializer, DjangoUserRegisterSerializer, DjangoUserSerializer, DjangoUserLoginSerializer, SendPasswordResetEmailSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class DjangoUserModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = DjangoUser.objects.all()
    serializer_class = DjangoUserSerializer
    # permission_classes = [ IsAuthenticated ]


class DjangoUserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = DjangoUserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user is not None:
                token = get_tokens_for_user(user)
                return SuccessResponse({'token': token}, 201)
            else:
                return ErrorResponse({'error': 'User Not Created'})
        return ErrorResponse({'error': serializer.errors})


class DjangoUserLoginView(APIView):
    def post(self, request, format=None):
        serializer = DjangoUserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            u_email = serializer.data.get('u_email')
            password = serializer.data.get('password')
            user = authenticate(u_email=u_email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return SuccessResponse(
                    {'token': token})
            else:
                return ErrorResponse({'user': 'User enable to login!'})


class DjangoUserChangePassWord(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = DjangUserChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            return SuccessResponse({'user': 'Password Has been Changed!'})
        return ErrorResponse(serializer.error)


class DjangoUserChangePassWordEmail(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return SuccessResponse({'message': 'Email sent successfully!'})
        return ErrorResponse(serializer.errors)


class DjangoUserPasswordResetView(APIView):
    def post(self, request, uid, token, format=None):
        serializer = DjangUserChangePasswordEmailWiseSerializer(
            data=request.data, context={'uid':  uid, 'token': token})

        if serializer.is_valid(raise_exception=True):
            return SuccessResponse({'message': 'Password updated!'})
        return ErrorResponse(serializer.errors)
