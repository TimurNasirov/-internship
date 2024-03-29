from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description', 'created_at', 'completed')
        model = Task