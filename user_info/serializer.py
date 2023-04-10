from django.contrib.auth.models import User
from rest_framework import serializers


class UserDescSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format='%Y-%m-%d %H:%M', required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_login',
            'email'
        ]
