from django.urls import path

from . import views

app_name = "product"

urlpatterns = [
    path("", views.search, name="search"),
    path("new/", views.add, name="new"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit/", views.edit, name="edit"),
]
