from rest_framework import serializers
from .models import Task





class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('creator',)

class GetTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('id','creator','assigner')
