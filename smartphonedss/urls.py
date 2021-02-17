from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='landing_page'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
]
