from django.urls import path,include
from .views import home,todo_list,delete,note_list,user_note_list



urlpatterns=[
    path('home',home,name='home'),
    path('all',todo_list,name="all"),
    path('delete/<slug:slug>',delete,name='delete'),
    path('notes/all',note_list,name='notes'),
    path('notes',user_note_list,name='user_notes'),



]