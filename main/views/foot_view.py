from rest_framework import viewsets, filters

from main import models, serializers
from utils import permissions
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
    permission_classes = [permissions.IsAdmin, permissions.IsWaiter]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'price']

    def get_queryset(self):
        print('user')
        return super().get_queryset()


class FoodReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API endpoint for managing foods.

        list:
        Return a list of all the foods.

        retrieve:
        Return the given food.
        """
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer
    pagination_class = CPageNumberPagination
    permission_classes = [permissions.IsAdmin, permissions.IsWaiter]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'price']

    def get_queryset(self):
        print('user')
        return super().get_queryset()
