from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    photo = models.ImageField(upload_to='images', auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
