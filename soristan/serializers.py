from soristan.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('name', 'surname', 'username', 'email', 'password')