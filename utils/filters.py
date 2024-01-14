import django_filters
from main import models
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = models.Order
        fields = ['status']

