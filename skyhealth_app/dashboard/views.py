from django.shortcuts import render

# Create your views here.

def is_admin(user):
    return user.is_staff

# renders admindashboard.html for only admins after verifying 

def admin_dashboard(request):
    if is_admin(request.user):
        return render(request, 'dashboard/admindashboard.html')

    
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')