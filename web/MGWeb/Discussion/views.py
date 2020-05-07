from django.shortcuts import render,redirect
from .models import Post
from .forms import MakePost
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,"disc/disc.html",{"posts":posts})

def create(request):
    if request.method == "POST":
        form = MakePost(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Discussion:home")


    else:
        form = MakePost()
    return render(request,"disc/create.html",{"form":form})