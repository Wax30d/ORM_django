from django.db import models


# 1 to 1 relationship
class Customer_1(models.Model):
    name = models.CharField(max_length=255)


class Vehicle_1(models.Model):
    name = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer_1,
        on_delete=models.CASCADE,
        related_name='vehicle'
    )


# 1 to many relationship
class Customer_2(models.Model):
    name = models.CharField(max_length=255)


class Vehicle_2(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer_2,
        on_delete=models.CASCADE,
        related_name='Vehicle'
    )
