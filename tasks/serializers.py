from rest_framework import serializers
from .models import Task
from accounts.models import User





class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('creator',)

class GetTaskSerializer(serializers.ModelSerializer):
    assigned_by = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id',"assigned_by",'title',"description","due_date","priority","status","created_at"]

    def get_assigned_by(self, obj):
        return obj.creator.username
