#Author - Arman Akond
#Co Author - Junayed Ahmed
#Co Author - Sikandar Ali


#Imports required for urls.py
from django.urls import path
from . import views



#All urls that are involved in voting
urlpatterns = [
    path('session/', views.session_view, name='session'),
    path('voting/', views.voting_view, name = 'voting' ),
    path('change_vote/<int:pk>/', views.change_vote_view, name='change_vote'),


]