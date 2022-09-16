"""jb_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from .views import DjangoUserChangePassWord, DjangoUserChangePassWordEmail, DjangoUserModelViewSet, DjangoUserLoginView, DjangoUserPasswordResetView, DjangoUserRegistrationView
from .user_views import UserViewSet
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'djangousers', DjangoUserModelViewSet, basename='django_user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', DjangoUserLoginView.as_view(), name='django_user_login'),
    path('register/', DjangoUserRegistrationView.as_view(),
         name='django_user_register'),
    path('change_password/', DjangoUserChangePassWord.as_view(),
         name='change_password'),
    path('send_reset_password_email/', DjangoUserChangePassWordEmail.as_view(),
         name='send_reset_password_email'),
    path('reset_password_by_email/<uid>/<token>',
         DjangoUserPasswordResetView.as_view(), name='reset_password_by_email'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
