from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class blogView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog/blog.html")
class blog1View(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog/a_bright_future.html")
class blog2View(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog/gene_drive.html")
class blog3View(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog/gene_editing.html")
