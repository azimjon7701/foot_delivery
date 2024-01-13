from rest_framework import serializers

from main import models


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = ['id', 'name', 'description', 'price', 'is_available']
