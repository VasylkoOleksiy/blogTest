from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=250)
    about=models.CharField(max_length=200, default="None")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.SlugField(max_length=200)
    updated=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    created=models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='img/',default='img/1.jpg') 


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('showPost', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created']