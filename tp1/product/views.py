from django.shortcuts import render
from .models import Product

def afficher_produits(request):
    produits = Product.objects.all()
    return render(request, "index.html", {
        "products": produits
        })




