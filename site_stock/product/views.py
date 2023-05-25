from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AddThingForm, EditThingForm
from .models import Category, Things

def search(request):
    """ Function for implementing the search for goods on the site and sorting by category """
    
    things = Things.objects.filter(is_sold=False)
    categories = Category.objects.all()
    if category_id:= request.GET.get("category", 0):
        things = things.filter(category_id=category_id)
    if search:= request.GET.get("search", ""):
        things = things.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )
    context = {
        "things": things,
        "categories": categories,
        "category_id": category_id,
        "search": search,
    }
    return render(request, "product/browse.html", context)


def detail(request, pk):
    """ Function that displays a personal page with a product """

    things = get_object_or_404(Things, pk=pk)
    related_things = Things.objects.filter(
        category=things.category, is_sold=False
    ).exclude(pk=pk)
    context = {"things": things, "related_things": related_things}
    return render(request, "product/detail.html", context)

@login_required
def add(request):
    """ Function that adds a thing to the site """

    if request.method == "POST":
        form = AddThingForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect("product:detail", pk=product.id)
    else:
        form = AddThingForm()
    context = {"form": form, "title": "New Thing"}
    return render(request, "product/new.html", context)

@login_required
def edit(request, pk):
    """ A function that edits the information of a thing on the site """
    
    things = get_object_or_404(Things, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = EditThingForm(request.POST, request.FILES, instance=things)
        if form.is_valid():
            form.save()
            return redirect("product:detail", pk=things.id)
    else:
        form = EditThingForm(instance=things)
    context = {
        "form": form,
        "title": "Edit item",
    }
    return render(request, "product/new.html", context)

@login_required
def delete(request, pk):
    """ A function that deletes a thing on the site """

    things = get_object_or_404(Things, pk=pk, created_by=request.user)
    things.delete()
    return redirect("store:index")