from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Things
from .forms import AddThingForm


def detail(request, pk):
    things = get_object_or_404(Things, pk=pk)
    related_things = Things.objects.filter(category=things.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {
        'things' : things,
        'related_things' : related_things
    }

    return render(request, 'product/detail.html', context)

@login_required
def add(request):
    if request.method == 'POST':
        form = AddThingForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()

            return redirect('product:detail', pk=product.id)
    else:
        form = AddThingForm()
    context = {
        'form': form,
        'title': 'New Thing'    
    }

    return render(request, 'product/new.html', context)