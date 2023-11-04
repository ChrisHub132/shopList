from django.shortcuts import render

from items.models import Category, Product

# Create your views here.
def index(request):
    products = Product.objects.all
    return render(request, 'core/index.html', {
        'products': products,
    })

def list(request):
    return render(request, 'core/list.html')
