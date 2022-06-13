from django.contrib import admin
from django.urls import path
from home import views
from rest_framework import routers

urlpatterns = [
    # path('',views.index, name="home" ),

    path('nav',views.nav, name="nav" ),
    path('index', views.index, name="index"),
  
    path('signup', views.signupuser, name="signupuser"),  
    path('login', views.loginuser, name="loginuser"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('', views.ApiOverview, name='home'), 


    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view_items'),
    path('update/<int:pk>/', views.update_items, name='update-items'),   
    path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),

]