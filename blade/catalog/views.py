from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = "blade/index.html"
    return render(request, template)


def catalog_list(request):
    return HttpResponse('Список товара')


def catalog_detail(request, pk):
    return HttpResponse(f"Товар {pk}")