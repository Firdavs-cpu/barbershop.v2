from pyexpat import model

from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()


class Booking(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()