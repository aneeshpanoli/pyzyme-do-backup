from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^home/', views.HomeView, name='HomeView'),
]
