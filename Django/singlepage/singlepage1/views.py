from django.http import Http404, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request) :
    return render (request, 'singlepage/index.html')

texts = ["itus bam delentique fabrique oh jet man lee france geek palm lottery phone",
         "bible father greeks of thick thug mug tweet farm greese friteer logtbber fight",
         "irish spring soap is levitating crime through live lessons primeer god of hype"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])

    else:
        raise Http404("No such section")