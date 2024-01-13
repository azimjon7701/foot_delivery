from rest_framework import viewsets, filters as rf
from django_filters.rest_framework import DjangoFilterBackend
from main import models, serializers
from utils import permissions, filters
from utils.paginators import CPageNumberPagination


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    pagination_class = CPageNumberPagination
    filterset_class = filters.OrderFilter
    permission_classes = [permissions.IsAdmin, permissions.IsWaiter]
    filter_backends = [DjangoFilterBackend,rf.OrderingFilter, rf.SearchFilter]
    ordering_fields = ['created_at', 'status']
    search_fields = ('food__name',)


