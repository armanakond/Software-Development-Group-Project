from django.urls import path
from . import views



urlpatterns = [
    path('session/', views.session_view, name='session'),
    path('voting/', views.voting_view, name = 'voting' ),
    
]

