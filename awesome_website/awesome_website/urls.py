# awesome_website/urls.py

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r"^", include("users.urls")),
    url(r"^admin/", admin.site.urls),
]