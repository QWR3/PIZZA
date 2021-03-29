from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from apps.user_profile.serializers import ProfileDetailSerializers

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    profile = ProfileDetailSerializers()

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'is_staff', 'is_superuser', 'is_active', 'profile']
