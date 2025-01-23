from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse
from .models import Product, Category


def product_list(request):
    """
    главная страница
    path('', views.catalog_list, name="product_list"),
    """
    categories = Category.objects.all()
    products = Product.objects.all()
    # показывать по 10 записей на странице
    paginator = Paginator(products, 12)
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    content = {
        "categories": categories,
        "page_obj": page_obj,
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
