from django.db import models


class Customer_1(models.Model):
    name = models.CharField(max_length=255)


class Vehicle_1(models.Model):
    name = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer_1,
        on_delete=models.CASCADE,
        related_name='vehicle'
    )
