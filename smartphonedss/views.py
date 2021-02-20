from django.shortcuts import render

def index(request):
   return render(request, 'index.html')

def login(request):
   print(request.method)
   context = {
      'page_title': "Halaman Login",
   }
   return render(request, 'login.html', context)

def register(request):
   context = {
      'page_title': "Halaman Register",
   }
   return render(request, 'register.html', context)

def register_preference(request):
   context = {
      'page_title': "Register Preferensi Pengguna"
   }
   return render(request, 'register-preference.html', context)

def register_success(request):
   context = {
      'page_title': "Berhasil Register"
   }
   return render(request, 'register-success.html', context)