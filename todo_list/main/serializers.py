from rest_framework import serializers

from .models import TaskModel, ToDoListModel, ToDoListGroupModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'


class ToDoListReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoListModel
        fields = ['id', 'name', 'tasks', 'todo_list_group']
        depth = 1


class ToDoListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoListModel
        fields = ['id', 'name', 'tasks', 'todo_list_group']


class ToDoListGroupModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoListGroupModel
        fields = ['id', 'description', 'todo_lists']
        depth = 1
