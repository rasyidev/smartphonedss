from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='landing_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('register-preference/', views.register_preference, name="register_preference"),
    path('register-success/', views.register_success, name="register_success"),
    path('logout/', views.user_logout, name='logout'),
    path('admin/', admin.site.urls),
]
