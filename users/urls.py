from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register_account/', views.register, name='register_account'),
    path('delete_account/', views.delete, name='delete_account'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
