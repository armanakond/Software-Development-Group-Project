from django.urls import path
from . import views

urlpatterns = [
    path('accountdetails/', views.accountdetails_view, name='accountdetails'), #names the path and calls accountdetails_view from views.py file
]