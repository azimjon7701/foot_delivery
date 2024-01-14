from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rf, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from main import models, serializers
from utils import permissions, filters
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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(user=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # def get_queryset(self):
    #     print('   ------   ', self.request.user)
    #     queryset = super().get_queryset().filter(user=self.request.user.id)
    #     return queryset
