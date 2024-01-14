from rest_framework import serializers

from main import models
from utils import helpers

order_time_answers = {
    'NEW': 'Order did not approved yet',
    'REJECTED': 'Order rejected',
    'DELIVERED': 'Order delivered'
}


class OrderSerializer:
    def get_estimated_time(self, instance: models.Order) -> str:
        if order_time_answers.get(instance.status):
            return order_time_answers.get(instance.status)
        time_seconds = instance.calculate_estimated_time()
        return helpers.format_time(time_seconds)


class OrderStaffSerializer(serializers.ModelSerializer, OrderSerializer):
    estimated_time = serializers.SerializerMethodField('get_estimated_time')
    class Meta:
        model = models.Order
        fields = ['id', 'food', 'user', 'price', 'status', 'distance', 'updated_at', 'description', 'estimated_time']
        read_only_fields = ['user', 'price']


class OrderUserSerializer(serializers.ModelSerializer, OrderSerializer):
    estimated_time = serializers.SerializerMethodField('get_estimated_time')

    def create(self, validated_data):
        validated_data.setdefault('user', self.context['request'].user)
        validated_data.setdefault('price', validated_data['food'].price)
        return super().create(validated_data)

    class Meta:
        model = models.Order
        fields = ['id', 'food', 'user', 'price', 'status', 'distance', 'updated_at', 'description', 'estimated_time']
        read_only_fields = ['user', 'price', 'status']
