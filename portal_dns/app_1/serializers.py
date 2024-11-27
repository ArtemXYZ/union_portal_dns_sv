from rest_framework.serializers import ModelSerializer

# _________________________________________
from app_1.models import Users


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ('code', 'full_name')