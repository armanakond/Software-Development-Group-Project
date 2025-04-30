from django.contrib import admin
from .models import AccountEntry, Team

# Register your models here.
@admin.register(AccountEntry)
class AccountEntryAdmin(admin.ModelAdmin):
    list_display      = ('name',)
    filter_horizontal = ('permissions',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',) 