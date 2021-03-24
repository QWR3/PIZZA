from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from apps.user_profile.serializers import ProfileSerializers

UserModel = get_user_model()


class RegisterSerializer(ModelSerializer):
    profile = ProfileSerializers()

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'profile']

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        serializers = ProfileSerializers(data=profile)
        serializers.is_valid(raise_exception=True)
        serializers.save(user=user)
        return user
