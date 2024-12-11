from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.loginPage, name='login'),
    path('register',views.registerPage,name='register'),
    path('profile/', views.profilePage, name='profile'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/edit/', views.edit_user_profile, name='edit_profile'),
    path('profile/update_profile', views.update_user_profile, name='update_profile')
]