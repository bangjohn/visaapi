from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"../templates/home.html")

def cekvisa(request):
    pass

def modal(request):
    return render(request,"../templates/modal.html")