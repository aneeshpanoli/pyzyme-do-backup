from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^iholdings/$', views.iholdingsView, name='iholdingsView'),
]
