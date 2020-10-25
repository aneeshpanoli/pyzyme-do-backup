from django.conf.urls.static import static
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import SubmitUrlForm
from static.py import pubmedGeneSearch
from django.views.generic import TemplateView

#------------------------------------------------------------------------------
class testView(TemplateView):
    template_name = "testProject/test.html"

class authorGeneHmView(View):
    def post(self, request, *args, **kwargs):
        # if "geneName" in request.POST:
        new_url = request.POST.get('geneName', False)
        new_url = new_url.lower()
        geneSearch = pubmedGeneSearch.mainPubmedSearch(new_url)
        if geneSearch == None:
            test = "There are no articles related to '%s' in the Pubmed database :(" % new_url
            context = {
                "newurl": test,
            }
            return render(request, "homepage/inv_keyword.html", context)
        # print new_url
        else:
        # ---table names-------
            test = "Here are the top genes connected to '%s'!" % new_url

            # countTotal = totalCount.total(table2name)

        # convert mysql to Json to use with D3

            context = {
                # "totalCount": countTotal,
                "title": "pyzyme.com",
                "newurl": test,
                # "authornames": tableSqloutput.outputTableContent(table3name),
            }
            return render(request, "testProject/geneAuthorHm.html", context)
