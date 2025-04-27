from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'accounts/registration.html') 

def register_view(request):
    return render(request, 'accounts/registration.html')

def login_view(request):
    return render(request, 'accounts/login.html')