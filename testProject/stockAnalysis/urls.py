from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^stock/', views.stockView, name='stockView'),
]
