from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.hello1, name='index1'),
]
