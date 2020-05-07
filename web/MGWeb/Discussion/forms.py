from django import forms
from .models import Post
class MakePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author","title","text"]