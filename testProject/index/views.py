from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "title": "pyzyme.com",
        }
        return render(request, "index/indexHome.html", context)

class disclaimView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "title": "pyzyme.com",
        }
        return render(request, "index/disclaimer.html", context)

class PrivacyPolicyView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "title": "pyzyme.com",
        }
        return render(request, "index/privacyPolicy.html", context)

class PrivacyPolicyAppView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "title": "pyzyme.com",
        }
        return render(request, "index/privacypolicyApp.html", context)
