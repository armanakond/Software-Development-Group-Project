from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('session/', include('voting.urls')),
    path('trends/', include('visualization.urls')),
    path('teamsummary/', include('visualization.urls'),)
]
