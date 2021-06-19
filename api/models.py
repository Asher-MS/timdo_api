from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    def __str__(self):
        return self.title
