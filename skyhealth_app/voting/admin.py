from django.contrib import admin
from .models import HealthVote


#admin.py code for healthvote part of application
@admin.register(HealthVote)
class HealthVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_name', 'session_date', 'team_name', 'submitted_at')
    list_filter = ('session_name', 'team_name')
    search_fields = ('user__username',)
