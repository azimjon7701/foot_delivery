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
    distance = models.FloatField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def calculate_estimated_time(self):
        delivery_time = self.distance * 3 * 60 if self.distance else 0
        if self.status == 'DELIVERING':
            return delivery_time
        before_orders = self.__class__.objects.filter(created_at__lte=self.created_at, status__in=['PENDING', 'APPROVED', 'COOKING'])
        before_orders_list = list(before_orders)
        chunk_size = 4
        chunks = [before_orders_list[i:i + chunk_size] for i in range(0, len(before_orders_list), chunk_size)]
        chunks_count = len(chunks)
        cooking_time = chunks_count * 5 * 60
        return cooking_time + delivery_time


    def __str__(self):
        return f'order: {self.id} - {self.status.lower()}'