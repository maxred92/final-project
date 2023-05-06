from django.urls import path

from . import views
from .views import FeedbackFormView, SuccessView

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', FeedbackFormView.as_view(), name='feedback'),
    path('success/', SuccessView.as_view(), name='success'),
]