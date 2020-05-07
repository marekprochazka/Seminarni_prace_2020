from .views import *
from django.urls import path

app_name = 'Discussion'

urlpatterns = [

  path("",home, name="home"),
  path("Tvorba",create,name="create")

]