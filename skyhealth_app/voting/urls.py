from django.urls import path
from . import views

urlpatterns = [
    path('voting/', views.session_view, name='voting'),
]