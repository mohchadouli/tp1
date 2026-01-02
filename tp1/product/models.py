from django.db import models

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
    ingredients = models.ManyToManyField(Ingredient, related_name="products")  # *-to-*

    def __str__(self):
        return self.Prd_Name