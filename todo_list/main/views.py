from django.http import Http404
from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView, ListAPIView

from .models import TaskModel, ToDoListModel
from .serializers import ToDoListTasksSerializer, ToDoListDetailedSerializer


def get_todo_list_items(todo_list_id, get_done_items=False):
    return TaskModel.objects.filter(todo_list=todo_list_id, is_done=get_done_items)


def get_todo_list(todo_list_id):
    todo_lists = ToDoListModel.objects.filter(id=todo_list_id)
    if not todo_lists:
        return None
    return todo_lists[0]


def todo_list_view(request, list_id):
    todo_list_items = get_todo_list_items(list_id)
    todo_list = get_todo_list(list_id)
    if not todo_list:
        raise Http404('No TODO list with id {id_}'.format(id_=list_id))
    return render(request, 'todo_list_details.html',
                  context={'todo_list': todo_list_items, 'todo_list_name': todo_list.name})


def completed_todos_view(request, list_id):
    todo_list_items = get_todo_list_items(list_id, get_done_items=True)
    todo_list = get_todo_list(list_id)
    if not todo_list:
        raise Http404('No TODO list with id {id_}'.format(id_=list_id))
    return render(request, 'completed_todo_list_details.html',
                  context={'todo_list': todo_list_items, 'todo_list_name': todo_list.name})


class ToDoListAPIView(ListAPIView):
    queryset = ToDoListModel.objects.all()
    serializer_class = ToDoListDetailedSerializer


class NotCompletedToDoListTasksAPIView(RetrieveAPIView):
    queryset = ToDoListModel.objects.prefetch_related('tasks').filter(tasks__is_done=False)
    serializer_class = ToDoListTasksSerializer
    lookup_url_kwarg = 'list_id'


class CompletedToDoListTasksAPIView(RetrieveAPIView):
    queryset = ToDoListModel.objects.prefetch_related('tasks').filter(tasks__is_done=True)
    serializer_class = ToDoListTasksSerializer
    lookup_url_kwarg = 'list_id'
