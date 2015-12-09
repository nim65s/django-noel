from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.secret_santa, name='secret_santa'),
)
