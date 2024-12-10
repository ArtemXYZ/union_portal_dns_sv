from rest_framework.serializers import ModelSerializer

# _________________________________________
from origin_site_basic.models import Users


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ('code', 'full_name')