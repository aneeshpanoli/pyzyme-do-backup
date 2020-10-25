from django.conf.urls.static import static
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
from .forms import SubmitUrlForm
from static.py import googleFinHistDown # causing lag
# Create your views here.
class stockView(TemplateView):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "pyzyme.com",
            "form": the_form,
        }
        return render(request, "stockAnalysis/query.html", context)
    # template_name = "stockAnalysis/query.html"
    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
            # return render(request, "loadingPage/loading.html")
        if form.is_valid():
            tickr = form.cleaned_data.get("url")
            days = form.cleaned_data.get("days")
            tickrjs = tickr.lower() + days
            tickr = tickr.lower()
            days = int(days)
            geneSearch = googleFinHistDown.main(tickr, days)

            context = {
                "tickr": tickrjs,
                "form": form,
            }
            return render(request, "stockAnalysis/results.html", context)
        else:
            test = "Invalid tickr"
            context = {
                "newurl": test,
            }
            return render(request, "homepage/inv_keyword.html", context)
