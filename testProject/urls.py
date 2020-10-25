from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^testp/', views.testView, name='testView'),
    url(r'^testpAgHm/', views.authorGeneHmView, name='authorGeneHmView'),
]
