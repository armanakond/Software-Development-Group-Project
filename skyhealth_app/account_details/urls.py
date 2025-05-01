from django.urls import path
from . import views

urlpatterns = [
    path('accountdetails/', views.accountdetails_view, name='accountdetails'), # calls accountdetails_view from views.py file so it can be redirected
]