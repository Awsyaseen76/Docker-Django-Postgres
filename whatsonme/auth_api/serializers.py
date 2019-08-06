from rest_framework import serializers
from . import models

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user_name', 'email', 'role', 'createdAt', 'updatedAt', 'role')
        model = models.Auth