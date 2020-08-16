from django.db import models

# Create your models here
class ProductData(models.Model):

    prodname = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics/')
    desc = models.TextField()
    oil = models.BooleanField(default=False)
    spices = models.BooleanField(default=False)
    foodcolor = models.BooleanField(default=False)
    grocery = models.BooleanField(default=False)

