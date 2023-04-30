from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('news.urls')),
    path('admin/', admin.site.urls),
] + staticfiles_urlpatterns()
