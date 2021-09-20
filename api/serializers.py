from rest_framework.serializers import ModelSerializer
from .models import Todo,Notes
from django.db.models import fields


class TodoSerializer(ModelSerializer):
    class Meta:
        model=Todo
        fields=['title','body','date','email']

class NoteSerializer(ModelSerializer):
    class Meta:
        model=Notes
        fields=['title','body','email']
