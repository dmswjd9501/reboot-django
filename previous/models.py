from django.db import models
# Create your models here.

class Previous(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    job = models.CharField(max_length=30)
