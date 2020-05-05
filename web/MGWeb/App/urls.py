from .views import *
from django.urls import path

app_name = 'App'

urlpatterns = [

    path("",home,name='home'),
    path("Prostredi",env,name='env'),
    path("Metody/Matematicka",gmMat,name="gmMat"),
    path("Metody/Kolac",gmPie,name="gmPie"),
    path("Metody/Sloupcovy",gmBar,name="gmBar"),
    path("Metody/Nahodny-sum",gmNo,name="gmNo"),
    path("Konzole",cons,name="cons"),
    path("Stazeni",down,name="down"),
    path("Diskuze",disc,name="disk"),
    path("O-autorovi",boutMe,name="boutMe")

]