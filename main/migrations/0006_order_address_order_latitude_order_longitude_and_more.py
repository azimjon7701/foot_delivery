# Generated by Django 4.0.5 on 2024-01-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_user_managers_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('NEW', 'new'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('PENDING', 'Pending'), ('COOKING', 'Cooking'), ('DELIVERING', 'Delivering'), ('DELIVERED', 'Delivered')], default='PENDING', max_length=20),
        ),
    ]
