from django.contrib import admin
from .models import AccountEntry

# Register your models here.
@admin.register(AccountEntry)
class AccountEntryAdmin(admin.ModelAdmin):
    list_display = ('created',)