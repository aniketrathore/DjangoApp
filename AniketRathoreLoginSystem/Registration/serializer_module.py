from rest_framework.serializers import ModelSerializer
from Registration.models import UserModel


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('full_name', 'username', 'email', 'password', 'dob', 'phone_no')
