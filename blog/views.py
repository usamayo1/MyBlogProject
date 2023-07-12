from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from .forms import SignupForm, PostForm, UserEditForm, ImageForm, LoginForm, PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Image

# Create your views here.

class SignupFormView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'blog/signup.html', {'form': form})
    
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        

def LoginView(request):
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                login(request, user=user)
                return redirect('home')
        return render(request, 'blog/login.html', {'form': form})
    return redirect('home')


def LogoutView(request):
    logout(request=request)
    return redirect('login')

@login_required(login_url='/login/')
def Changepassword(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
    return render(request, 'blog/changepass.html', {'form': form})

default_img = '/media/default.jpg'

@login_required(login_url='/login/')
def ProfileView(request):
    pform = UserEditForm(instance=request.user)
    if request.method == "POST":
        pform = UserEditForm(instance=request.user, data=request.POST)
        if pform.is_valid():
            pform.save()
    iform = ImageForm()
    if request.method == 'POST':
        iform = ImageForm(request.POST, request.FILES)
        if iform.is_valid():
            instance = iform.save(commit=False)
            instance.user = request.user
            instance.save()
    
    context = {'pform': pform, 'iform': iform, 'default': default_img}
    image = None
    try:
        image = Image.objects.get(user=request.user.id)
    except:
        pass
    if image is not None:
        context['image'] = image
    
    return render(request, 'blog/profile.html', context)


@login_required(login_url='/login/')
def HomepageView(request):        
    posts = Post.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
    try:
        images = Image.objects.all()
    except:
        return HttpResponse("This code does not work to display images")
    
    context = {'posts': posts, 'form': form, 'images': images, 'default': default_img}
    return render(request, 'blog/home.html', context)

def EditPost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.user != post.author:
        return HttpResponse('You are not allowed here!')
    if request.method == 'POST':
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'blog/home.html', {'form': form})
    
    
def DeletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.user != post.author:
        return HttpResponse('You are not allowed here!')
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog/deletepost.html', {'obj': post})


