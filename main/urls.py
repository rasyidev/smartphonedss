from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('user-preferences/', views.user_preferences, name='user_preferences'),
    path('register-preference/', views.register_preference, name='register_preference'),
    path('profile/', views.profile, name='profile'),
]
