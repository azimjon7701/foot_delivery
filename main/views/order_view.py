from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rf, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from main import models, serializers
from utils import permissions, filters
from utils.current_user import get_current_user_id
from utils.paginators import CPageNumberPagination


class OrderStaffViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    """
        API endpoint for managing orders.

        list:
        Return a list of all the orders.

        retrieve:
        Return the given order.

        update:
        Update the given order.

        partial_update:
        Partially update the given order.

    """
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderStaffSerializer
    pagination_class = CPageNumberPagination
    filterset_class = filters.OrderFilter
    permission_classes = [permissions.IsWaiter]
    filter_backends = [DjangoFilterBackend, rf.OrderingFilter, rf.SearchFilter]
    ordering_fields = ['created_at', 'status']
    search_fields = ('food__name',)





class OrderUserViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    """
        API endpoint for managing orders.

        list:
        Return a list of all the orders.

        create:
        Create a new order.

        retrieve:
        Return the given order.

        update:
        Update the given order.

        partial_update:
        Partially update the given order.

    """
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderUserSerializer
    pagination_class = CPageNumberPagination
    filterset_class = filters.OrderFilter
    permission_classes = [permissions.IsCustomer]
    filter_backends = [DjangoFilterBackend, rf.OrderingFilter, rf.SearchFilter]
    ordering_fields = ['created_at', 'status']
    search_fields = ('food__name',)


    def get_queryset(self):
        print('   ------   ', get_current_user_id())
        queryset = super().get_queryset().filter(user_id=get_current_user_id())
        return queryset
