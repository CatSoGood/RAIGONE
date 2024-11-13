from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    name = "admin"
    return render(request,"index.html",{"name":name})

def template (request):
    return render(request, "template.html")

def dashboard(request):
    return render(request, "dashboard.html")