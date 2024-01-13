from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
