from django.urls import path,include
from .views import home,todo_list,delete



urlpatterns=[
    path('home',home,name='home'),
    path('all',todo_list,name="all"),
    path('delete/<slug:slug>',delete,name='delete'),



]