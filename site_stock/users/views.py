from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse, reverse_lazy

from product.models import Things


from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/users/login/')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {
        'form': form
    })

def profile(request):
    things = Things.objects.filter(created_by=request.user)

    return render(request, 'users/profile.html', {
        'things': things,
    })
