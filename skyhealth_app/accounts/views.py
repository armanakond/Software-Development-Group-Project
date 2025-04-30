from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'accounts/registration.html') 

def register_view(request):
    if request.method == 'POST':
        # 1) pull the form values
        first_name = request.POST['first_name']
        username   = request.POST['username']
        email      = request.POST['email']
        password   = request.POST['password']

        # 2) simple duplicate-check
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, 'accounts/registration.html')

        # 3) create & save
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.first_name = first_name
        user.save()

        # 4) redirect to login
        return redirect('login')

    # GET just shows the blank form
    return render(request, 'accounts/registration.html', )


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            #log in and send to dashboard
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    # if GET, or failed POST renders
    return render(request, 'accounts/login.html')