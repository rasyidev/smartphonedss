from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from . import ahp_logic
from .models import UserPreference, CustomUser

# Create your views here.
# @login_required
def index(request):
   preferences = UserPreference.objects.filter(user_id=request.user.id)
   preference_empty = None
   if len(preferences) == 0:
      print("Smartphone Preference not registered yet!")
      preference_empty = True
   else:
      preference_empty = False

   context = {
      'page_title': "Dashboard",
      'preference_empty': preference_empty,
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

def profile(request):
   user = request.user
   preferences = UserPreference.objects.filter(user_id=user.id)
   preference_empty = None
   if len(preferences) == 0:
      print("Smartphone Preference not registered yet!")
      preference_empty = True
   else:
      preference_empty = False
      preferences = preferences[0]
   context = {
      'preference_empty': preference_empty,
      'page_title': "User Profile",
      'preferences': preferences
   }
   return render(request, 'profile.html', context)

def register_preference(request):
   # print(request.user.id)
   # print(UserPreference.objects.all()[0].__dict__)
   print(request.user.id)
   form_result = None
   if request.method == "POST":
      form_result = request.POST or None
     
      performance_vs_price = form_result['performance_vs_price']
      performance_vs_camera = form_result['performance_vs_camera']
      performance_vs_memory = form_result['performance_vs_memory']
      performance_vs_battery = form_result['performance_vs_battery']
      performance_vs_reputation = form_result['performance_vs_reputation']
      price_vs_camera = form_result['price_vs_camera']
      price_vs_memory = form_result['price_vs_memory']
      price_vs_battery = form_result['price_vs_battery']
      price_vs_reputation = form_result['price_vs_reputation']
      camera_vs_memory = form_result['camera_vs_memory']
      camera_vs_battery = form_result['camera_vs_battery']
      camera_vs_reputation = form_result['camera_vs_reputation']
      memory_vs_battery = form_result['memory_vs_battery']
      memory_vs_reputation = form_result['memory_vs_reputation']
      battery_vs_reputation = form_result['battery_vs_reputation']
      
      apapun = dict(form_result.copy())
      apapun.pop('csrfmiddlewaretoken')
      print(apapun)
      ahp = ahp_logic.AHP(apapun, 6)
      # print("Object in AHP:", ahp.obj)
      print(ahp.is_consistent())
      if ahp.is_consistent():

         # delete previous preference
         user_preference = UserPreference.objects.filter(user_id=request.user.id)
         if len(user_preference) >= 1:
            for preference in user_preference:
               preference.delete()

         cw = ahp.get_criteria_weight()
         UserPreference.objects.create(user=CustomUser.objects.get(id=request.user.id), performance=cw[0], price=cw[1], camera=cw[2], memory=cw[3], battery=cw[4], reputation=cw[5])

         return redirect('dashboard:profile')
      else:
         print( ahp.get_criteria_weight())
         return redirect('dashboard:register_preference')

   range_value = list(range(-9,10))
   range_value.remove(-1)
   range_value.remove(0)

   form_input_data = [
      {'name': 'performance_vs_price', 'left':'Performa', 'right':'Harga'},
      {'name': 'performance_vs_camera', 'left':'Performa', 'right':'Kamera'},
      {'name': 'performance_vs_memory', 'left':'Performa', 'right':'Kapasitas Memori Internal'},
      {'name': 'performance_vs_battery', 'left':'Performa', 'right':'Kapasitas Baterai'},
      {'name': 'performance_vs_reputation', 'left':'Performa', 'right':'Reputasi Produk'},
      {'name': 'price_vs_camera', 'left':"Harga", 'right': "Kamera"},
      {'name': 'price_vs_memory', 'left':"Harga", 'right': "Kapasitas Memori Internal"},
      {'name': 'price_vs_battery', 'left':"Harga", 'right': "Kapasitas Baterai"},
      {'name': 'price_vs_reputation', 'left':"Harga", 'right': "Reputasi Produk"},
      {'name': 'camera_vs_memory', 'left':'Kamera', 'right':'Kapasitas Memori Internal'},
      {'name': 'camera_vs_battery', 'left':'Kamera', 'right':'Kapasitas Baterai'},
      {'name': 'camera_vs_reputation', 'left':'Kamera', 'right':'Reputasi Produk'},
      {'name': 'memory_vs_battery', 'left':'Kapasitas Memori Internal', 'right':'Kapasitas Baterai'},
      {'name': 'memory_vs_reputation', 'left':'Kapasitas Memori Internal', 'right':'Reputasi Produk'},
      {'name': 'battery_vs_reputation', 'left':'Kapasitas Memori Internal', 'right':'Reputasi Produk'},
      # {'name': 'ram_vs_cpu', 'left':'RAM', 'right':'CPU'},
      # {'name': 'rating_vs_sold', 'left':'Rating', 'right':'Jumlah Produk Terjual'}
   ]

   context = {
      'range_value': range_value,
      'input': form_input_data,
      'form_result' : form_result,
      'page_title': "Register Preferensi Pengguna"
   }
   return render(request, 'register-preference.html', context)