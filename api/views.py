from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets,permissions
import urllib.parse


def home(req):
    return HttpResponse("HOME")
def delete(req,slug):
    print(urllib.parse.unquote(slug))
    if(Todo.objects.filter(title=urllib.parse.unquote(slug))):
        print(urllib.parse.unquote(slug))
        pass
    else:
        print(urllib.parse.unquote(slug))
        return JsonResponse({"status":"unable to delete"})
    try:
        print(urllib.parse.unquote(slug))
        Todo.objects.filter(title=urllib.parse.unquote(slug)).delete()
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

