from pyexpat import model

from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    def __str__(self):
        return self.name