from django.utils.encoding import force_bytes, smart_str

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from xml.dom import ValidationErr

from rest_framework import serializers

from utils.email import Utils

from .models import DjangoUser


class DjangoUserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = DjangoUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ['id']

    def create(self, validated_data):
        user = DjangoUser.objects.create_user(**validated_data)
        return user


class DjangoUserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = DjangoUser
        fields = ["u_email", "u_name", "u_mobile", "u_billingname", "u_role",
                  "isactive", "is_admin", "is_active", "isdelete", "password", "password2"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password doesn't match")
        return attrs

    def create(self, validated_data):
        user = DjangoUser.objects.create_user(**validated_data)
        return user


class DjangoUserLoginSerializer(serializers.ModelSerializer):
    u_email = serializers.EmailField(max_length=255)

    class Meta:
        model = DjangoUser
        fields = ["id", "u_email", "password"]


class DjangUserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')

        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs


class SendPasswordResetEmailSerializer(serializers.Serializer):
    u_email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['u_email']

    def validate(self, attrs):
        u_email = attrs.get('u_email')
        if DjangoUser.objects.filter(u_email=u_email).exists():
            user = DjangoUser.objects.get(u_email=u_email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'http://localhost:8000/user/reset_password_by_email/' + uid + '/' + token

            # data = {
            #     'to': user.email,
            #     'subject': 'Reset Password Link',
            #     'body': link
            # }

            # Utils.send_mail(data)
            return attrs
        else:
            ValidationErr('You are not Register!')


class DjangUserChangePasswordEmailWiseSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        uid = self.context.get('uid')
        token = self.context.get('token')

        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password doesn't match")

        id = smart_str(urlsafe_base64_decode(uid))
        user = DjangoUser.objects.get(id=id)

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise ValidationErr('Token has been expired!')
        user.set_password(password)
        user.save()
        return attrs
