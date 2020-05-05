from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html")


def env(request):
    return render(request, "env.html")


def gmMat(request):
    return render(request, "gm-mat.html")


def gmPie(request):
    return render(request, "gm-Pie.html")


def gmBar(request):
    return render(request, "gm-bar.html")


def gmNo(request):
    return render(request, "gm-no.html")


def cons(request):
    return render(request, "cons.html")

def down(request):
    return render(request,"down.html")

def disc(request):
    return render(request,"disc.html")

def boutMe(request):
    return render(request,"boutme.html")