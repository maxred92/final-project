from django.shortcuts import render, get_object_or_404

from .models import Things


def detail(request, pk):
    things = get_object_or_404(Things, pk=pk)
    related_things = Things.objects.filter(category=things.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {
        'things' : things,
        'related_things' : related_things
    }

    return render(request, 'product/detail.html', context)