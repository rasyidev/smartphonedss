from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.db.models.functions import Lower
import json

from . import ahp_logic
from .models import UserPreference, CustomUser, Smartphone, Product, Cart, SmartphoneCart, ProductRecommendation

# Create your views here.
@login_required
def index(request):
   smartphones = Smartphone.objects.all().order_by('name')
   if request.method == "POST":
      searchkey = request.POST['searchbar'].lower()
      s = Smartphone.objects.annotate(lower_name=Lower('name'))
      smartphones = s.filter(lower_name__contains = searchkey)
   
   for smartphone in smartphones:
      # print(smartphone.id)
      product = Product.objects.filter(smartphone_model_id=smartphone.id)
      # smartphones['stock'] = len(product)

   preferences = UserPreference.objects.filter(user_id=request.user.id)
   preference_empty = None
   if len(preferences) == 0:
      print("Smartphone Preference is not registered yet!")
      preference_empty = True
   else:
      preference_empty = False

   context = {
      'smartphones': smartphones,
      'page_title': "Dashboard",
      'preference_empty': preference_empty,
   }
   return  render(request, 'dashboard.html', context)

@login_required
def user_logout(request):
   logout(request)
   return redirect('/')

@login_required
def user_preferences(request):
   user = request.user
   preferences = UserPreference.objects.filter(user_id=user.id, is_choosen=True)[0]
   context = {
      'page_title': "Preferensi Smartphone",
      'preferences': preferences,
   }
   return render(request, 'user-preference.html', context)

@login_required
def profile(request):
   user = request.user
   preferences = UserPreference.objects.filter(user_id=user.id)
   cart = Cart.objects.filter(user_id=user.id)
   # smartphone_objects = SmartphoneCart.objects.filter(cart_id=cart.id)
   # smartphones = []
   # for x in smartphone_objects:
   #    smartphones.append(Smartphone.objects.get(id=x.smartphone_id))
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
      'preferences': preferences,
      'cart': cart,
   }
   return render(request, 'profile.html', context)

@login_required
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

         return redirect('dashboard:index')
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

@login_required
def get_smartphones(request):
   smartphones = Smartphone.objects.all()
   
   data = {}
   if request.method == "GET":
      # tanpa pencarian 
      if len(request.GET) > 0:
         search_key= request.GET['search_key']
         s = Smartphone.objects.annotate(lower_name=Lower('name'))
         smartphones = s.filter(lower_name__contains=search_key)
         smartphones = serializers.serialize('json', smartphones)
         # print(smartphones)
         data = {
            'smartphones': smartphones
         }
         
   return JsonResponse(data)

@login_required
def insert_to_cart(request):
   response = ""
   # if request get data exist
   if len(request.GET) > 0:
      smartphone_id = request.GET['smartphone_id']
      smartphone = Smartphone.objects.get(id=smartphone_id)
      user_id = request.user.id
      # print("User id:", user_id)

      # user have no cart -> create one
      if len(Cart.objects.filter(user_id=user_id, do_recommendation=False)) < 1:
         print("User have no cart")
         Cart.objects.create(user_id=user_id, do_recommendation=False)
         cart = Cart.objects.filter(user_id=user_id, do_recommendation=False)[0]

         #check if smartphone is already exist in SmartphoneCart
         already_exist = False
         if len(SmartphoneCart.objects.filter(cart_id=cart.id, smartphone_id=smartphone.id)) > 0:
            already_exist = True
         
         if already_exist is False:
            SmartphoneCart.objects.create(cart_id=cart.id, smartphone_id=smartphone_id)
            response = f"Berhasil menambahkan data {smartphone.name}"
         else:
            response = "Smartphone sudah ada di dalam keranjang"

      # else (user have cart)
      else:
         print("User already have a cart")
         cart = Cart.objects.filter(user_id=user_id, do_recommendation=False)[0]

         #check if smartphone is already exist in SmartphoneCart
         already_exist = False
         if len(SmartphoneCart.objects.filter(cart_id=cart.id, smartphone_id=smartphone.id)) > 0:
            already_exist = True

         if already_exist is False:
            SmartphoneCart.objects.create(cart_id=cart.id, smartphone_id=smartphone_id)
            response = f"Berhasil menambahkan data {smartphone.name}"
         else:
            response = "Smartphone sudah ada di dalam keranjang"

      
   else:
      response = "Gagal menambahkan data smartphone"


   return redirect('dashboard:index')

@login_required
def remove_from_cart(request):
   response = ""
   # if request get data exist
   if len(request.GET) > 0:
      smartphone_id = request.GET['smartphone_id']
      user_id = request.user.id
      cart = Cart.objects.filter(user_id=user_id, do_recommendation=False)[0]
      smartphonecart = SmartphoneCart.objects.filter(cart_id=cart.id)
      smartphone_tobe_removed = SmartphoneCart.objects.get(smartphone_id=smartphone_id, cart_id=cart.id)
      smartphone_name = Smartphone.objects.get(id=smartphone_id).name
      # print(smartphone_tobe_removed.__dict__)
      smartphone_tobe_removed.delete()
      response = f"{smartphone_name} has removed from your cart!"
      return redirect('dashboard:cart')

   else:
      response = "No data to be removed!"
   return HttpResponse(response)
   # return redirect('dashboard:profile')

@login_required
def rekomendasi(request):
   if request.method == "POST":
      print(request.POST)

   user_id = request.user.id
   cart = Cart.objects.filter(user_id=user_id, do_recommendation=False)[0]
   smartphonecart = SmartphoneCart.objects.filter(cart_id=cart.id)
   smartphone_ids = []
   for smartphone in smartphonecart:
      smartphone_ids.append(smartphone.smartphone_id)
   # print("smartphone ids:", smartphone_ids)

   products = Product.objects.filter(smartphone_model_id__in=smartphone_ids)
   p = UserPreference.objects.get(user_id=user_id)
   data = []
   for product in products:
      smartphone = Smartphone.objects.get(id=product.smartphone_model_id)
      obj = {}
      obj['smartphone_id'] = smartphone.id
      obj['product_name'] = smartphone.name
      obj['product_id'] = product.id
      obj['seller'] = product.seller
      obj['ram'] = smartphone.ram
      obj['storage'] = smartphone.storage
      obj['cpu'] = smartphone.cpu
      obj['battery'] = smartphone.battery
      obj['main_cam'] = smartphone.main_cam
      obj['selfie_cam'] = smartphone.selfie_cam
      obj['price'] = product.price
      obj['rank'] = product.rank
      obj['score'] = 0
      obj['product_url'] = product.product_url
      data.append(obj)

   normalized_data = []
   max_ram =max(x['ram'] for x in data)
   max_storage =max(x['storage'] for x in data)
   max_cpu =max(x['cpu'] for x in data)
   max_battery =max(x['battery'] for x in data)
   max_main_cam =max(x['main_cam'] for x in data)
   max_selfie_cam =max(x['selfie_cam'] for x in data)
   min_price = min(x['price'] for x in data)
   min_rank = min(x['rank'] for x in data)

   for product in data:
      obj = {}
      obj['product_name'] = product['product_name']
      obj['product_id'] = product['product_id']
      obj['ram'] = product['ram'] / max_ram
      obj['storage'] = product['storage'] / max_storage
      obj['cpu'] = product['cpu'] / max_cpu
      obj['battery'] = product['battery'] / max_battery
      obj['main_cam'] = product['main_cam'] / max_main_cam
      obj['selfie_cam'] = product['selfie_cam'] / max_selfie_cam
      obj['price'] = min_price / product['price']
      obj['rank'] = min_rank / product['rank']
      obj['score'] = (
          (product['ram'] / max_ram) ** (0.5 * p.performance/100) +
         (product['cpu'] / max_cpu) ** (0.5 * p.performance/100) +
         (product['storage'] / max_storage) ** (p.memory/100) +
         (product['battery'] / max_battery) ** (p.battery/100) +
         (product['main_cam'] / max_main_cam) ** (0.5 * p.camera/100) +
         (product['selfie_cam'] / max_selfie_cam) ** (0.5 * p.camera/100) +
         (min_price / product['price']) ** (p.price/100) +
         (min_rank / product['rank']) ** (p.reputation/100)
      )
      normalized_data.append(obj)

   print(normalized_data[0])
   # print("Max CPU", max_cpu)
   for idx,obj in enumerate(data):
      obj['score'] = normalized_data[idx]['score']

   data = sorted(data, key=lambda x: x['score'])
   data.reverse()



   # TOP 20
   ids = set([x['smartphone_id'] for x in data])
   each_model_amount = 20 // len(ids)
   left_amount = 20 - each_model_amount * len(ids)

   obj = {}
   for id in ids:
      obj[str(id)] = []

   for x in data:
      for id in ids:
         if x['smartphone_id'] == id:
               obj[str(id)].append(x)

   top_20 = []
   keys = list(obj.keys())
   first_key = keys[0]
   if left_amount > 0:
      top_20 += obj[first_key][:(each_model_amount + left_amount)]
   else:
      top_20 += obj[k][:each_model_amount]
   for k in keys[1:]:
      top_20 += obj[k][:each_model_amount]

   # sort by score
   top_20 = sorted(top_20, key=lambda x: x['score'])
   top_20.reverse()
   # with open('extracted_data.json', 'w') as f:
   #    json.dump(data, f)
   # print("data0", data[0]['cpu'])
   context = {
      'page_title': "Rekomendasi",
      'data': data,
      'top5': top_20[:5],
      'topnext15': top_20[5:20]
   }

   return render(request, 'rekomendasi.html', context)

@login_required
def cart(request):
   user = request.user
   smartphones = []
   preferences = UserPreference.objects.filter(user_id=user.id)
   if len(Cart.objects.filter(user_id=user.id, do_recommendation=False)) > 0:
      cart = Cart.objects.filter(user_id=user.id, do_recommendation=False)[0]

      smartphone_objects = SmartphoneCart.objects.filter(cart_id=cart.id)
      for x in smartphone_objects:
         smartphones.append(Smartphone.objects.get(id=x.smartphone_id))

   context = {
       'page_title': "Keranjang Smartphone",
       'preferences': preferences,
       'smartphones': smartphones,
   }

   return render(request, 'cart.html', context)

@login_required
def recommendation_result(request):
   user_id = request.user.id

   cart = Cart.objects.filter(user_id = user_id, do_recommendation=False)[0]
   
   data = {}
   if request.method == "POST":
      data = dict(request.POST)

   del data['csrfmiddlewaretoken']
   
   data_keys = list(data.keys())


   products = []
   # len(data_keys)
   for i in range(0, len(data_keys), 3):
      is_relevant, product_id, score = data_keys[i:i+3]
      obj = {}
      obj['is_relevant'] = bool(int(data[is_relevant][0]))
      obj['product_id'] = data[product_id][0]
      obj['score'] = float(data[score][0])
      products.append(obj)
   
   for idx, x in enumerate(products):
      # print(x, product[x])
      ProductRecommendation.objects.create(order=idx+1, product_id=x['product_id'], cart_id=cart.id, relevance=x['is_relevant'], score=x['score'])
   
   cart.do_recommendation = True
   cart.save()



   context = {
      'cart': cart,
      'message': "Produk rekomendasi berhasil disimpan."
   }

   return render(request, 'recommendation_result.html', context)


def cart_details(request):
   if request.method == "GET":
      cart_id = request.GET['cart_id']
      user_id = request.user.id
      cart = Cart.objects.get(id=cart_id)
      products = []
      product_recommendations = ProductRecommendation.objects.filter(cart_id=cart_id)
      for pr in product_recommendations:
         product = Product.objects.get(id=pr.product_id)
         smartphone = Smartphone.objects.get(id=product.smartphone_model_id)
         obj = {}
         obj['product_name'] = smartphone.name
         obj['product_id'] = product.id
         obj['seller'] = product.seller
         obj['ram'] = smartphone.ram
         obj['storage'] = smartphone.storage
         obj['cpu'] = smartphone.cpu
         obj['battery'] = smartphone.battery
         obj['main_cam'] = smartphone.main_cam
         obj['selfie_cam'] = smartphone.selfie_cam
         obj['price'] = product.price
         obj['rank'] = product.rank
         obj['score'] = 0
         obj['product_url'] = product.product_url
         obj['relevance'] = pr.relevance
         products.append(obj)

   # products = serializers.serialize('json', products)
   context = {
      'page_title': "Detail Keranjang",
      'products': products
   }
   return render(request, 'cart_details.html', context)
      
   #output: cart and its products

def default_preference(request):
   user_id = request.user.id
   p = UserPreference.objects.get(user_id=user_id)
   p.performance = 6.67
   p.price = 6.67
   p.camera = 6.67
   p.memory = 6.67
   p.battery = 6.67
   p.reputation = 6.67
   p.is_choosen = True
   p.save()

   context = {
      'page_title': "Preferensi Standar",
   }
   return render(request, 'default_preference.html')
