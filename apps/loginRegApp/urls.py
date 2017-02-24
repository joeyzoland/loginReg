from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validator$', views.validator),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]
