from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets,permissions


def home(req):
    return HttpResponse("HOME")
def delete(req,slug):
    if(Todo.objects.filter(title=slug)):
        pass
    else:
        return JsonResponse({"status":"unable to delete"})
    try:
        Todo.objects.filter(title=slug).delete()
        return JsonResponse({"status":"deleted"})
    except:
        pass


    

class TodoViewSet(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    permissions_classes=[permissions.AllowAny]

todo_list=TodoViewSet.as_view({
    'get':'list',
    'post':'create'
})

