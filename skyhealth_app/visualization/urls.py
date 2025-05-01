#Author: Arman
from django.urls import path
from . import views

urlpatterns = [
    path('trends/', views.trends_view, name='trends'), # renders visualization/trends.html from templates
    path('teamsummary/', views.teamsummary_view, name='teamsummary'), # renders visualization/teamsummary.html from templates
]