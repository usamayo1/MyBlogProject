from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post, Image


class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-box', 'placeholder': 'Password'}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-box', 'placeholder': 'Password again'}), label="")
    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {'email': '', 'username': ''}
        
        widgets = {
            'username':forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Username'}),
            'email':forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Email'})
        }
            
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Username'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Password'}), label='')
    

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