from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('hallo/', include('first.urls')),
    path('temp/', include('temp.urls')),
    path('admin/', admin.site.urls),
]
