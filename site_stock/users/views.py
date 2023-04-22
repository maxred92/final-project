from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse, reverse_lazy


from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse('store:index'))
        else:
            form = SignUpForm()
    return render(request, 'users/signup.html', {
        'form': form
    }) 
