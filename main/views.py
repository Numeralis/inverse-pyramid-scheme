from django.shortcuts import render
from .models import Product

# Create your views here.
def show_app(request):
    products = Product.objects.all()
    context = {
        'app'       : 'main',
        'name'      : 'Meinhard Christian',
        'class'     : 'PBP E',
        'products'  : products
    }

    return render(request, "main.html", context)