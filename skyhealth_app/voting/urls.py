#Author - Junayed Ahmed
#Co Author - 
#Co Author - 


from django.urls import path
from . import views



urlpatterns = [
    path('session/', views.session_view, name='session'),
    path('voting/', views.voting_view, name = 'voting' ),
    path('change_vote/<int:pk>/', views.change_vote_view, name='change_vote'),


]