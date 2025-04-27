from django.shortcuts import render

# Create your views here.

def is_admin(user):
    return user.is_staff

def admin_dashboard(request):
    return render(request, 'dashboard/admindashboard.html')


def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')