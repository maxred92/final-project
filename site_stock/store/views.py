from django.shortcuts import render, redirect

from product.models import Category, Things

def index(request):
    things = Things.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'categories' : categories,
        'things' : things,
    }
    return render(request, 'store/index.html', context)

def contact(request):
    return render(request, 'store/contact.html')