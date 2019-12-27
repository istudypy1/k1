from django.conf.urls import include, url

from django.contrib import admin


urlpatterns = [
    url(r'^pages/', include('pages.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),

]




