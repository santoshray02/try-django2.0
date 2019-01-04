from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def home(request):
    context = {"name" : "Santosh Ray"}
    return render(request, 'index.html', context)