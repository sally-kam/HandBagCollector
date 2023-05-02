from django.db import models

# Create your models here.
class Handbag(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image = models.CharField(max_length=200)