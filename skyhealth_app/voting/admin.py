#Author - Md Hoque
#Co Author - Junayed Ahmed

#All necessary imports required for admin.py and its functionalities
from django.contrib import admin
from .models import HealthVote
from .models import Session, Team


#admin.py code for healthvote part of application
@admin.register(HealthVote)
class HealthVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_name', 'session_date', 'team_name', 'submitted_at') 
    list_filter = ('session_name', 'team_name') # can be edited on django dashboard
    search_fields = ('user__username',)


#admin.py code for Session Admin
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    ordering = ('date',)

#admin.py code for Team Admin
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)