from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    text_var = 'This is my first django app web page.'
    return HttpResponse(text_var)