from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product


# def index(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "product/index.html", context)


def product_list(request):
    """
    path('', views.catalog_list, name="product_list"),
    """
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product/product_list.html", context)


def product_detail(request, pk):
    return HttpResponse(f"Товар {pk}")
