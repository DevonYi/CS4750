from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
# Create your views here.

def home(request):
    """Renders the home page."""
    print("home")
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        context={
            'title': 'Home Page',
        }
    )

