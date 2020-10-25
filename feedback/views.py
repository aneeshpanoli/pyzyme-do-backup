from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class feedbackView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "title": "pyzyme.com",
        }
        return render(request, "feedback/feedback.html", context)
