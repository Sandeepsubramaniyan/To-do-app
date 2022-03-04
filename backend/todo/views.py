from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Todoserializer
from .models import Todo
 

class TodoView(viewsets.ModelViewSet):
    serializer_class = Todoserializer
    queryset = Todo.objects.all()
    
    
    
