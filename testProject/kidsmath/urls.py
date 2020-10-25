from django.urls import path
from . import views
urlpatterns = [
    path('api/kidsmath/predict-post', views.predict_request, name='predict_digit'),
    path('api/biodictchat/predict-get', views.predict_response, name='predict_response'),
]
