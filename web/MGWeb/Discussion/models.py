from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100, default="auth")
    title = models.CharField(max_length=100,default="title")
    text = models.TextField(max_length=1000)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}, {self.title}...{self.date} "

    def snippet(self):
        return f"{self.text[:50]}..."