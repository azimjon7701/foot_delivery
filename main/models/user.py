from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE = (
        ('ADMIN', 'admin'),
        ('WAITER', 'waiter'),
        ('CUSTOMER', 'customer'),
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
    )
    username = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=10, null=True, choices=ROLE)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email', 'username']

    def get_name(self):
        if self.first_name and self.last_name:
            return f"{self.last_name} {self.first_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.__str__()
