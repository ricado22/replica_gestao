from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('startup.urls', namespace='startup')),

    path('admin/', admin.site.urls),
]

