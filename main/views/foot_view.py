from rest_framework import viewsets, filters

from main import models, serializers
from utils.paginators import CPageNumberPagination


class FoodViewSet(viewsets.ModelViewSet):
    """
        API endpoint for managing foods.

        list:
        Return a list of all the foods.

        create:
        Create a new food.

        retrieve:
        Return the given food.

        update:
        Update the given food.

        partial_update:
        Partially update the given food.

        destroy:
        Delete the given food.
        """
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer
    pagination_class = CPageNumberPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'price']
