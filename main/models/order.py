from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'new'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('PENDING', 'Pending'),
        ('COOKING', 'Cooking'),
        ('DELIVERING', 'Delivering'),
        ('DELIVERED', 'Delivered')
    ]
    food = models.ForeignKey("main.Food", on_delete=models.CASCADE, related_name="orders")
    user = models.ForeignKey("main.User", on_delete=models.SET_NULL, null=True, related_name="orders")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)