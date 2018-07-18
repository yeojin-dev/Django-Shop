from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products_by_category, name='all_products'),
    path(
        '<str:category_slug>/',
        views.all_products_by_category,
        name='all_products_by_category'
    ),
]
