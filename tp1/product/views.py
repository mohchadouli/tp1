from django.shortcuts import render
from .models import Product

def afficher_produits(request):
    produits = Product.objects.all()
    return render(request, "index.html", {
        "products": produits
        })

def rechercher_produit(request):
    if request.method == "GET":
        query = request.GET.get('search')
        if query:
            produits = Product.objects.filter(Prd_Name__contains=query)
            return render(request, 'search.html', {
                'products': produits
            })
    return render(request, 'search.html')



