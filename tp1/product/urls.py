from django.urls import path
from . import views

urlpatterns = [
    path('list_products/', views.afficher_produits, name='list_products'),
    path('search_product/', views.rechercher_produits, name='search_product'),
    path('commander/', views.commander_prd, name='commander'),
]