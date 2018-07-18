from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def index(request):
    text_var = 'This is my first django app web page.'
    return HttpResponse(text_var)


def all_products_by_category(request, category_slug=None):
    category_page = None
    products = None

    if category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=category_page,
            available=True,
        )
    else:
        products = Product.objects.all().filter(available=True)

    context = {
        'category': category_page,
        'products': products,
    }

    return render(request, 'shop/category.html', context)
