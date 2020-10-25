from django.conf.urls.static import static
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import SubmitUrlForm
from static.py import pubmedGeneSearch
from django.db import connection
import os
import pandas as pd
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class indexView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "pyzyme.com",
            "form": the_form,
        }
        return render(request, "homepage/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if request.method == 'POST' and 'searchform' in request.POST.keys():
            if form.is_valid():
                new_url = form.cleaned_data.get("url")
                new_url = new_url.lower()
                csv_file_name = "static/csv/pubmed/"+new_url+".csv"
                csv_path = os.path.join(BASE_DIR, csv_file_name)
                try:
                    if datetime.fromtimestamp(os.path.getmtime(csv_path)).date() < datetime.now().date():
                        geneSearch = pubmedGeneSearch.mainPubmedSearch(new_url)
                    else:
                        geneSearch = "good"
                except:
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
                    df = pd.read_csv(csv_path)
                    author_name = df['authors'].tolist()
                    article_count = df['authorsCount'].tolist()
                    gene_name =  df["genes"].tolist()
                    gene_count = df["genesCount"].tolist()

                    master_list = [{'author':t[0], 'a_count':t[1], 'gene':t[2], 'g_count':t[3]} \
                                    for t in zip(author_name, article_count, gene_name, gene_count)]

                    test = "Here are the top people and genes connected to '%s'!" % new_url

                    context = {
                        "title": "pyzyme.com",
                        "datalist": master_list,
                        "form": form,
                        "newurl": test,
                        "geneName": new_url,
                    }
                    return render(request, "homepage/results.html", context)


            else:
                context = {
                    "title": "pyzyme.com",
                    "form": form
                }
                return render(request, "homepage/home.html", context)
        elif request.method == 'POST' and 'geneFunction' in request.POST.keys():
            context = {
                "title": "pyzyme.com",
                "post_dtails": request.POST['geneFunction']
            }
            return HttpResponse()
        else:
            context = {
                "title": "pyzyme.com",
                "form": form,
                "post_dtails": request.POST.keys()
            }
            return render(request, "homepage/results.html", context)
