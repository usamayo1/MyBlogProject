from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Post, Image


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {'email': 'Email'}
        
class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'email': 'Email'}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['photo']
        labels = {'photo': ''}