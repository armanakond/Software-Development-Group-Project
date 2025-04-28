from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
]