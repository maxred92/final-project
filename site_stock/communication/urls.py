from django.urls import path

from . import views

app_name = 'communication'

urlpatterns = [
    path('new/<int:things_pk>/', views.new_communication, name='new'),
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]