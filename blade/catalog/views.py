from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная страницы")


def catalog_list(request):
    return HttpResponse('Список товара')


def catalog_detail(request, pk):
    return HttpResponse(f"Товар {pk}")