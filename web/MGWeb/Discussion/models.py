from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100, default="auth")
    title = models.CharField(max_length=100,default="title")
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, db_index=True,default="")



    def __str__(self):
        return f"{self.author}, {self.title}...{self.date} "

    def snippet(self):
        return f"{self.text[:50]}..."

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
