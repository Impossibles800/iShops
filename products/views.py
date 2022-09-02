from django.shortcuts import render

from products.models import Category
from .models import Product


# Create your views here.
def home(request):
    category = Category.objects.all().values()
    product = Product.objects.all()
    categorires = {
        'categ': category,
        'product': product,
    }
    return render(request, 'products.html', categorires)


def show_category(request, pkid):
    show_categ = Category.objects.get(pk=pkid)
    #
    categ = Category.objects.all().values()
    product = Product.objects.filter(category=show_categ)
    data = {
        'product': product,
        'categ': categ,
    }
    #

    return render(request, 'products.html', data)


def search(request):
    find = request.GET['find']
    products = Product.objects.filter(title__icontains=find)
    data_1 = {
        'products': products
    }
    return render(request, 'result.html', data_1)