from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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