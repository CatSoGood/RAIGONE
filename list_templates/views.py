from django.shortcuts import render
from django.http import HttpResponse
from list_templates.models import orders

name = "Chonchanin"

def index (request):
    return render(request,"index.html")

def template (request):
    all_orders = orders.objects.all()
    return render(request, "template.html", {"name":name, "all_orders":all_orders})

def dashboard(request):
    all_orders = orders.objects.all()
    return render(request, "dashboard.html", {"name":name, "all_orders":all_orders})