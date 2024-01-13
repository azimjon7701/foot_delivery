from rest_framework import serializers

from main import models


class OrderSerializer(serializers.ModelSerializer):
    estimated_time = serializers.SerializerMethodField('get_estimated_time')

    def get_estimated_time(self, instance: models.Order) -> str:
        return "20 minutes"

    def create(self, validated_data):
        validated_data.setdefault('user', self.context['request'].user)
        validated_data.setdefault('price', validated_data['food'].price)
        return super().create(validated_data)

    class Meta:
        model = models.Order
        fields = ['id', 'food', 'user', 'price', 'status',
                  'created_at', 'updated_at', 'description', 'estimated_time']
        read_only_fields = ['user', 'price', 'status']
