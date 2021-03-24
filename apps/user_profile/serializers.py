from rest_framework.serializers import ModelSerializer
from .models import ProfileModel


class ProfileSerializers(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['id', 'name', 'surname', 'age']


class ProfileDetailSerializers(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['id', 'name', 'surname', 'age', 'avatar']
