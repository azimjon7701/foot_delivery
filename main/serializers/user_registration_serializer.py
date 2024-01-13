from rest_framework import serializers

from main import models


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['phone_number', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        validated_data.setdefault('role', 'CUSTOMER')
        user = models.User.objects.create_user(**validated_data)
        return user
