from django.conf.urls import url

from . import views

app_name = 'secret_santa'
urlpatterns = [
        url(r'^$', views.secret_santa, name='secret_santa'),
        ]
