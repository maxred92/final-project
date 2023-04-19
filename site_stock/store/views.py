from django.shortcuts import render

def index(request):
    return render(request, 'store/index.html')

def contact(request):
    return render(request, 'store/contact.html')