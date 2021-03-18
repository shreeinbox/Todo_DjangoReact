
from rest_framework import serializers
from .models import Task

#Serializer for model Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
