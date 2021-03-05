from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='landing_page'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('register-preference/', views.register_preference, name="register_preference"),
    path('register-success/', views.register_success, name="register_success"),
    path('dashboard/', include('main.urls', namespace='dashboard')),
    path('admin/', admin.site.urls),
]
