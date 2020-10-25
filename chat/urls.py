from django.urls import path
from . import views
urlpatterns = [
    path('api/biodictchat/biodict-get', views.message_list, name='message-detail'),
    path('api/biodictchat/biodict-post', views.message_list, name='message-list'),
    path('api/biodictchat/usercheck-post', views.user_exists, name='checkuser'),
    path('api/biodictchat/validateuser-post', views.validate_user, name='validateuser'),

]
