from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Lunch(models.Model):
    name = models.CharField(max_length=64)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=256)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=48, default="Protein")
    rating = models.IntegerField(default=0)


    def __str__(self):
        return self.name

