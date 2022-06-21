from django.contrib import admin
from django.urls import path
from home import views
from rest_framework import routers

urlpatterns = [
    path('',views.index, name="home" ),

    path('nav',views.nav, name="nav" ),
    path('index', views.index, name="index"),
    path('demo', views.demo, name="demo"),
    path('userpage', views.userpage, name="userpage"),
    path('videos', views.videos, name="videos"),
    path('logout', views.logoutUser, name="logoutUser"),
    # path('login', views.loginuser, name="loginuser"),

  
    path('signup', views.signupuser, name="signupuser"),  
    path('login/', views.login, name="login"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
    # path('api/', views.ApiOverview, name='home'), 

    # path('studentcreate/', views.student_create, name='student_create'),
    # path('studentdetails/', views.student_details, name='student_details'),



    path('create/', views.add_items, name='add_items'),
    path('all/', views.view_items, name='view_items'),
    # path('update/<int:pk>/', views.update_items, name='update_items'),   
    path('item/<int:pk>/delete/', views.delete_items, name='delete_items'),

]