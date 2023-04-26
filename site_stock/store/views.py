from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from product.models import Category, Things

def index(request):
    things = Things.objects.filter(is_sold=False)
    categories = Category.objects.all()
    paginator = Paginator(things, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
    context = {
        'categories' : categories,
        'things' : things,
        'posts': posts,
        'page': page,
    }
    return render(request, 'store/index.html', context)

def contact(request):
    return render(request, 'store/contact.html')