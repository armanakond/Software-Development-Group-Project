from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('dashboard.urls')),
    path('', include('voting.urls')),
    path('', include('visualization.urls')),
    path('', include('account_details.urls')),
]
