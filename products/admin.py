from django.contrib import admin
from products.models import *

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Basket)
