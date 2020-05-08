from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import MakePost,MakeComment
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-date')
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

def detail(request,slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = MakeComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("Discussion:detail",slug=slug)

    else:
        form = MakeComment()
        comments = Comment.objects.filter(post=post).order_by('-date')

    return render(request,"disc/post.html",{"post":post,"comments":comments,"form":form})