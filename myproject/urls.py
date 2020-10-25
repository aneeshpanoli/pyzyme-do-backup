
# do not startapp in virtual env
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from homepage.views import indexView
from index.views import HomeView, disclaimView, PrivacyPolicyView, PrivacyPolicyAppView
from detail.views import detailView
from testProject.views import testView
from testProject.views import authorGeneHmView
from loadingPage.views import loadingView
from stockAnalysis.views import stockView
from blog.views import blogView, blog1View, blog2View, blog3View
from feedback.views import feedbackView
from iholdings.views import iholdingsView
from chat.views import message_list, user_exists, validate_user
from kidsmath.views import predict_request, predict_response
from genomeedit.views import GeditView


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^disclaimer/', disclaimView.as_view()),
    url(r'^privacypolicy/', PrivacyPolicyView.as_view()),
    url(r'^privacypolicyapp/', PrivacyPolicyAppView.as_view()),
    url(r'^home/', indexView.as_view()),
    url(r'^detail/', detailView.as_view()),
    url(r'^testp/', testView.as_view()),
    url(r'^testpAgHm/', authorGeneHmView.as_view()),
    url(r'^loading/', loadingView.as_view()),
    url(r'^stock/', stockView.as_view()),
    url(r'^blog/$', blogView.as_view()),
    url(r'^blog/1$', blog1View.as_view()),
    url(r'^blog/2$', blog2View.as_view()),
    url(r'^blog/3$', blog3View.as_view()),
    url(r'^feedback/$', feedbackView.as_view()),
    url(r'^iholdings/$', iholdingsView.as_view()),
    url(r'^genomeedit/', GeditView.as_view()),
    # url(r'^genomeedit/', genomeeditView.as_view()),
    #rest_framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/biodictchat/biodict-get', message_list, name='message-detail'),
    path('api/biodictchat/biodict-post', message_list, name='message-list'),
    path('api/biodictchat/usercheck-post', user_exists, name='checkuser'),
    path('api/biodictchat/validateuser-post', validate_user, name='validateuser'),
    path('api/kidsmath/predict-post', predict_request, name='predict_digit'),
    path('api/biodictchat/predict-get', predict_response, name='predict_response'),
]
