from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, EmailActivateView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='tokens'),
    path('/activate', EmailActivateView.as_view(), name='activate user'),
    path('/refresh', TokenRefreshView.as_view(), name='refresh tokens'),
    path('/register', RegisterView.as_view(), name='register user')
]
