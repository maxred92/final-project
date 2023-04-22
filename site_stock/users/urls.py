from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginUserForm

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(next_page='store:index', template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='store:index'), name='logout'),
]