from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('challenges.urls')),  # Include challenges app URLs
    # Keep other paths if needed, or replace TemplateView with app views
]