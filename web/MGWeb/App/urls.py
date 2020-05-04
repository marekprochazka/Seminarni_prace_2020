from .views import *
from django.urls import path

app_name = 'App'

urlpatterns = [

    path("",home,name='home'),
    path("env",env,name='env')
]