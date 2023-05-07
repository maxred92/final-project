from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from product.models import Category, Things

from .forms import FeedbackForm

""" Displaying all products and connecting pagination """


def index(request):
    things = Things.objects.filter(is_sold=False)
    categories = Category.objects.all()
    paginator = Paginator(things, 3)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {
        "categories": categories,
        "things": things,
        "posts": posts,
        "page": page,
    }
    return render(request, "store/index.html", context)


def contact(request):
    return render(request, "store/contact.html")


""" Implementation of sending feedback """


class FeedbackFormView(FormView):
    template_name = "store/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "store/success.html"
