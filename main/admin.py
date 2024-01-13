from django.contrib import admin
from django.contrib.auth.hashers import make_password

from main import models


# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    model = models.User
    list_display = ['email', 'phone_number']

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            raw_password = form.cleaned_data['password']
            obj.password = make_password(raw_password)
        super().save_model(request, obj, form, change)


admin.site.register(models.User, CustomUserAdmin),
admin.site.register(models.Food)
