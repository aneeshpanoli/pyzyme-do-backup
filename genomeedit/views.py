from django.shortcuts import render
from django.views import View


class GeditView(View):
    def get(self, request, *args, **kwargs):
        context = {"Title" : "pyzyme.com"}
        return render(request, "genomeedit/gedit.html", context)

# Create your views here.
