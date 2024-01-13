from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):

    def _create_user(self, phone_number, email, password, **extra_fields):
        """
        Create and save a user with the given phone_number, email, and password.
        """
        if not phone_number:
            raise ValueError("The given phone_number must be set")
        email = self.normalize_email(email)

        user = self.model(
            phone_number=phone_number,
            email=email,
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, email, password, **extra_fields)


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

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email', 'username']

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def get_name(self):
        if self.first_name and self.last_name:
            return f"{self.last_name} {self.first_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.__str__()
