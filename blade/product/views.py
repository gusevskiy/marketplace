from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse
from .models import Product, Category, ProductImage
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    """
    главная страница
    path('', views.catalog_list, name="product_list"),
    """
    category = None
    categories = Category.objects.all()
    # products = Product.objects.filter(available=True)
    products = Product.objects.all()
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        print("category_slug", category_slug)
    # показывать по 10 записей на странице
    paginator = Paginator(products, 12)
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    content = {
        "categories": categories,
        "page_obj": page_obj,
        "category": category,
        'cart_product_form': cart_product_form,
    }
    return render(request, "product/product_list.html", content)


def product_detail(request, id, slug):
    """
    Указанный экземпляр
    можно получить только по id, так как это уникальный атрибут. Однако
    в URL-адрес еще включается slug, чтобы формировать дружественные для
    поисковой оптимизации URL-адреса товаров.
    """
    product = get_object_or_404(Product, id=id, slug=slug)
    images = product.images.all()
    cart_product_form = CartAddProductForm()
    content = {
        'product': product,
        'cart_product_form': cart_product_form,
        'images': images
    }
    return render(request, 'product/product_detail.html', content)
