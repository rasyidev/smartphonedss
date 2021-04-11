from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('user-preferences/', views.user_preferences, name='user_preferences'),
    path('register-preference/', views.register_preference, name='register_preference'),
    path('profile/', views.profile, name='profile'),
    path('rekomendasi/', views.rekomendasi, name='rekomendasi'),
    path('get_smartphones', views.get_smartphones, name="get_smartphones"),
    path('insert_to_cart', views.insert_to_cart, name="insert_to_cart"),
    path('remove_from_cart', views.remove_from_cart, name="remove_from_cart"),
    path('cart', views.cart, name="cart"),
    path('recommendation_result', views.recommendation_result, name="recommendation_result"),
    path('profile/cart_details', views.cart_details, name="cart_details"),
    path('profile/default_preference', views.default_preference, name="default_preference"),
]
