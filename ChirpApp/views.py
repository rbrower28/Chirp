from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'ChirpApp/index.html', {

    })