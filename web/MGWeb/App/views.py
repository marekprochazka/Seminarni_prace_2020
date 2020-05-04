from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")

def env(request):
    return render(request,"env.html")
