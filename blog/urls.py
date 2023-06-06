from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupFormView.as_view(), name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('changepass/', views.Changepassword, name='changepass'),
    path('home/', views.HomepageView, name='home'),
    path('profile/', views.ProfileView, name='profile'),
    path('edit/<int:pk>/', views.EditPost, name='editpost'),
    path('deletepost/<int:pk>/', views.DeletePost, name='deletepost'),

]