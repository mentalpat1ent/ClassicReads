from django.urls import path
from . import views

urlpatterns = [
    path('', views.quotes, name='quotes'),
    path('homepage/', views.homepage, name='homepage'),
    path('discover/', views.discover, name='discover'),
    path('mybooks/', views.mybooks, name='mybooks'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('signup/', views.aboutus, name='signup'),
    path('success/', views.success_page, name='success_page'), 
    path("dashboard/", views.dashboard, name="dashboard"),

]