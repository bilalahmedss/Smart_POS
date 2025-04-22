from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the default password reset URLs from Django's auth system
    path('accounts/', include('django.contrib.auth.urls')),
]
