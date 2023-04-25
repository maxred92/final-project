from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Things, Category
from .forms import AddThingForm, EditThingForm


def search(request):
    things = Things.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    search = request.GET.get('search', '')

    if category_id:
        things = things.filter(category_id=category_id)

    if search:
        things = things.filter(Q(name__icontains=search) | Q(description__icontains=search))
    

    context = {
        'things' : things,
        'categories' : categories,
        'category_id': category_id,
        'search': search

    }
    return render(request, 'product/browse.html', context)


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


@login_required
def edit(request, pk):
    things = get_object_or_404(Things, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditThingForm(request.POST, request.FILES, instance=things)

        if form.is_valid():
            form.save()

            return redirect('product:detail', pk=things.id)
    else:
        form = EditThingForm(instance=things)
    context = {
        'form': form,
        'title': 'Edit item',}
    return render(request, 'product/new.html', context
    )

@login_required
def delete(request, pk):
    things = get_object_or_404(Things, pk=pk, created_by=request.user)
    things.delete()

    return redirect('store:index')