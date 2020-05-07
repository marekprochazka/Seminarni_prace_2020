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
        print(form)
        if form.is_valid():
            form.save()
            return redirect("Discussion:home")


    else:
        form = MakePost()
    return render(request,"disc/create.html",{"form":form})

def detail(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request,"disc/post.html",{"post":post})