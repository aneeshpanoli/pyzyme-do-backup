from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^blog/$', views.blogView, name='blogView'),
    url(r'^blog/1$', views.blog1View, name='a_bright_future'),
    url(r'^blog/2$', views.blog2View, name='gene_drive'),
]
