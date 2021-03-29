from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from rest_framework.serializers import ModelSerializer, CharField

from apps.user_profile.serializers import ProfileSerializers
from enums.regex_enum import RegEx as R
from apps.auth_.utils import Utils

UserModel = get_user_model()


class RegisterSerializer(ModelSerializer):
    profile = ProfileSerializers()
    password = CharField(validators=[
        RegexValidator(R.PASSWORD.reg, R.PASSWORD.msg)
    ], write_only=True)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'profile']

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        token = Utils.create_email_token(user)
        data = {
            'subject': 'activat accaunt',
            'body': f'https://localhost:4200/activate?token={token}',
            'to': [user.email]

        }
        Utils.send_mail(**data)
        serializers = ProfileSerializers(data=profile)
        serializers.is_valid(raise_exception=True)
        serializers.save(user=user)
        return user
