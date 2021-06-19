from rest_framework.serializers import ModelSerializer
from .models import Todo
from django.db.models import fields


class TodoSerializer(ModelSerializer):
    class Meta:
        model=Todo
        fields=['title','body','date']