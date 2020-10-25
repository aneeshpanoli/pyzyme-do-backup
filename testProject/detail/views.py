from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class detailView(View):
    # if request.method == 'POST':

    def post(self, request):
        if request.method == 'POST':
            # details = request.POST.get('geneName', False)
            details = request.POST['geneName']
            context = {
                "newurl": details,
            }
            return render(request, "detail/detail.html", context)
