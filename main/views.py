from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import UserPreference, CustomUser

# Create your views here.
# @login_required
def index(request):
   context = {
      'page_title': "Dashboard"
   }
   return  render(request, 'dashboard.html', context)

# @login_required
def user_logout(request):
   logout(request)
   return redirect('/')

def user_preferences(request):
   user = request.user
   preferences = UserPreference.objects.filter(user_id=user.id, is_choosen=True)[0]
   context = {
      'page_title': "Preferensi Smartphone",
      'preferences': preferences,
   }
   return render(request, 'user-preference.html', context)