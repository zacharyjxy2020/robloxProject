from django.shortcuts import render

# Create your views here.
def index(request):
    """
        As a single page app, many links and routes will default to index.
        This will render the single html used, outside of the login and register pages.
    """
    return render(request, "RobloxInputSite/index.html")