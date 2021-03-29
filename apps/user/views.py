from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, UpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .permissions import IsSuperUser

from .serializers import UserSerializer

# Create your views here.
from ..user_profile.serializers import ProfileDetailSerializers

UserModel = get_user_model()


class UserListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserApToAdmin(GenericAPIView):
    queryset = UserModel.objects.all()

    permission_classes = [IsSuperUser]

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UpdateUserProfileView(UpdateAPIView):
    serializer_class = ProfileDetailSerializers

    def get_permissions(self):
        pk = self.kwargs.get('pk')
        if self.request.user.id != pk:
            return [IsAdminUser()]
        return [IsSuperUser()]

    def get_object(self):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        return user.profile
