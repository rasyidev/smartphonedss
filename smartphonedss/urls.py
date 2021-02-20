from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='landing_page'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register-preference/', views.register_preference, name="register_preference"),
    path('register-success/', views.register_success, name="register_success"),
    path('admin/', admin.site.urls),
]
