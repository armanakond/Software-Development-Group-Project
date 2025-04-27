from django.urls import path
from . import views

urlpatterns = [
    path('trends/', views.trends_view, name='trends'),
    path('', views.teamsummary_view, name='teamsummary'),
]