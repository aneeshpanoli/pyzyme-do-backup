from django.conf.urls import include, url
from . import views



urlpatterns = [
    url(r'^detail/', views.detailView, name='detailView'),
]
