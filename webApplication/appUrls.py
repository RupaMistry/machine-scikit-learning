"""webApplication URL Configuration

# webApplication/appUrls.py
from django.conf.appUrls import include, url
from django.contrib.auth import views
from webApplication import basic_views


urlpatterns = [
    url(r'', include('portalApp.appUrls'))
]
