# Author - Md - Created the sub sections of the "Accounts" and allowed those fields to be able to handle inputted data
# Co-Author -
# Co-Author -

from django.contrib import admin
from .models import AccountEntry, Team


# Register your models here.
@admin.register(AccountEntry)
class AccountEntryAdmin(admin.ModelAdmin):
    list_display      = ('name',)
    filter_horizontal = ('permissions',)

# displays the name of team records.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',) 