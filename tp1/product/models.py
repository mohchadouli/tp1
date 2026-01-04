from django.db import models
from django.utils import timezone


class Category(models.Model):
    Cat_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Cat_Name


class Ingredient(models.Model):
    Ing_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Ing_Name


class Product(models.Model):
    Prd_Name = models.CharField(max_length=100)
    Price = models.FloatField()
    Created_at = models.DateTimeField(auto_now=True)
    ID_Cat = models.ForeignKey(Category, on_delete=models.CASCADE)  # 1-to-*
    ingredients = models.ManyToManyField(
        Ingredient, related_name="products")  # *-to-*

    def __str__(self):
        return self.Prd_Name


class Commande(models.Model):
    Description_cmd = models.CharField(max_length=50)
    # Note: default=timezone.now
    Date_cmd = models.DateField(default=timezone.now)
    Produit_cmd = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.Description_cmd
