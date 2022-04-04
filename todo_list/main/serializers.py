from rest_framework import serializers

from .models import TaskModel, ToDoListModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'


class ToDoListTasksSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer

    class Meta:
        model = ToDoListModel
        fields = ['tasks']
        depth = 1


class ToDoListDetailedSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer

    class Meta:
        model = ToDoListModel
        fields = ['id', 'name', 'tasks']
        depth = 1