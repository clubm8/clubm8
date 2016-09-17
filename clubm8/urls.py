from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('clubm8web.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('clubm8api.urls')),
]
