from django.shortcuts import render
from .models import Product

def afficher_produits(request):
    produits = Product.objects.all()
    return render(request, "index.html", {
        "products": produits
        })

def rechercher_produits(request):
    if request.method == "GET":
        query = request.GET.get('search')
        if query:
            # Niveau 1: Search in product names
            produits_n1 = Product.objects.filter(Prd_Name__contains=query)
            
            if produits_n1.exists():
                return render(request, 'search.html', {'products': produits_n1, 'level': 1})
            else:
                # Niveau 2: Search in ingredients
                produits_n2 = Product.objects.filter(ingredients__Ing_Name__contains=query)
                return render(request, 'search.html', {
                    'products': produits_n2,
                    'level': 2,
                    'query': query
                })
    
    return render(request, 'search.html')




