from django.db import models

class Product(models.Model):
    product_image = models.ImageField()
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_rate = models.FloatField()
    product_availability = models.BooleanField()

class Review(models.Model):
    text = models.CharField(max_length=256)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)