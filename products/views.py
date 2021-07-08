from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required

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
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),

    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product, quantity=1)
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
