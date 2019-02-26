from django.db import models


# Create your models here.

class Cocktails(models.Model):
    name = models.CharField(max_length=200)
    alcohol_percentage = models.DecimalField(default=0)
    serving_glass = models.IntegerField(default=0)
