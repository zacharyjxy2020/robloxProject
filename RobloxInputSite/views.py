from django.shortcuts import render
import json
from django.http import JsonResponse
from .src.handle import collectData


# Create your views here.
def index(request):
    """
        As a single page app, many links and routes will default to index.
        This will render the single html used, outside of the login and register pages.
    """
    return render(request, "RobloxInputSite/index.html")

def htmlReq(request) :
    if request.method == "GET":
        x = collectData()
        return JsonResponse({
            "success" : x
        }, safe= False)
    else:
        return JsonResponse({
            "error" : "no data"
        }, status = 400)