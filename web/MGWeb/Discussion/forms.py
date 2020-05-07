from django import forms
from .models import Post
class MakePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author","title","text"]
    def clean(self):
        if self.is_valid():
            title = self.cleaned_data["title"]
            if Post.objects.filter(title=title).exists():
                raise forms.ValidationError("Title already exists")
