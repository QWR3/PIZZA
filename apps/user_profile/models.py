from django.contrib.auth import get_user_model
from django.db import models
from django.core import validators as v

from .services import avatar_upload
from enums.profile_enums import REGEXP_NAME

UserModel = get_user_model()


# Create your models here.
class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=25, validators=[
        v.RegexValidator(REGEXP_NAME, 'Only alpha min 2 max 20')
    ])
    surname = models.CharField(max_length=25, validators=[
        v.RegexValidator(REGEXP_NAME, 'Only alpha min 2 max 20')
    ])
    age = models.IntegerField(validators=[
        v.MinValueValidator(14),
        v.MaxValueValidator(150)
    ])
    avatar = models.ImageField(upload_to=avatar_upload)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
