from django.shortcuts import render, redirect
from .models import Product
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_app')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)