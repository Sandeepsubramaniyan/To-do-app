from rest_framework import serializers
from .models import Todo


class Todoserializer(serializers.Modelserializer):
    class Meta:
        model = Todo
        fields = ('id','title','description','completed')
        
        