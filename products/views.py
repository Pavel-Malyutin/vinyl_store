from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'VinylStore',
        'h1_header': 'VinylStore - проигрыватели, пластинки и аксессуары',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'VinylStore - каталог товаров',
        'h1_header': 'VinylStore',
    }
    return render(request, 'products/products.html', context)

