from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from .models import Product, Category


def product_list(request):
    """
    path('', views.catalog_list, name="product_list"),
    """
    categories = Category.objects.all()
    products = Product.objects.all()
    content = {
        "categories": categories,
        "products": products,
        "selected_category": None
    }
    return render(request, "product/product_list.html", content)


def product_list_by_category(request, category_slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    content = {
        "categories": categories,
        "products": products,
        "selected_category": category_slug
    }
    return render(request, "product/product_list.html", content)


def product_detail(request, pk):
    return HttpResponse(f"Товар {pk}")
