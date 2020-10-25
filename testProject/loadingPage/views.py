from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class loadingView(TemplateView):
    template_name = "loadingPage/loading.html"
