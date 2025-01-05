from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product/index.html", context)


def catalog_list(request):
    return HttpResponse("Список товара")


def catalog_detail(request, pk):
    return HttpResponse(f"Товар {pk}")
