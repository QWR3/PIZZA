from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView

from .serializers import UserSerializer

# Create your views here.

UserModel = get_user_model()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
