from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from rest_framework.response import Response
from .models import Todo,Notes
from .serializers import TodoSerializer,NoteSerializer
from rest_framework import viewsets,permissions
import urllib.parse


def home(req):
    return HttpResponse("HOME")
def delete(req,slug):
    print(urllib.parse.unquote(slug)    )
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


class NoteViewSet(viewsets.ModelViewSet):
    queryset=Notes.objects.all()
    serializer_class=NoteSerializer
    permissions_classes=[permissions.AllowAny]


note_list=NoteViewSet.as_view({
    'get':'list',
    'post':'create'
})

class UserNoteViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        email=self.request.query_params.get('email')
        print(email)
        try:
            queryset=Notes.objects.filter(email=email)
        except:
            pass
        return queryset
    serializer_class=NoteSerializer
    permissions_classes=[permissions.AllowAny]
    

user_note_list=UserNoteViewSet.as_view({
    'get':'list',
    'post':'create',
})


    