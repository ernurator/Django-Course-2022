import logging

from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from .models import TaskModel, ToDoListModel, ToDoListGroupModel
from .serializers import TaskSerializer, ToDoListReadSerializer, ToDoListCreateSerializer, ToDoListGroupModelSerializer

logger = logging.getLogger(__name__)


def get_todo_list_items(todo_list_id, get_done_items=False):
    return TaskModel.objects.filter(todo_list=todo_list_id, is_done=get_done_items)


def get_todo_list(todo_list_id):
    todo_lists = ToDoListModel.objects.filter(id=todo_list_id)
    if not todo_lists:
        return None
    return todo_lists[0]


def todo_list_view(request, list_id):  # Deprecated
    todo_list_items = get_todo_list_items(list_id)
    todo_list = get_todo_list(list_id)
    if not todo_list:
        raise Http404('No TODO list with id {id_}'.format(id_=list_id))
    return render(request, 'todo_list_details.html',
                  context={'todo_list': todo_list_items, 'todo_list_name': todo_list.name})


def completed_todos_view(request, list_id):  # Deprecated
    todo_list_items = get_todo_list_items(list_id, get_done_items=True)
    todo_list = get_todo_list(list_id)
    if not todo_list:
        raise Http404('No TODO list with id {id_}'.format(id_=list_id))
    return render(request, 'completed_todo_list_details.html',
                  context={'todo_list': todo_list_items, 'todo_list_name': todo_list.name})


class NotCompletedToDoListTasksAPIView(ListAPIView):  # Deprecated
    queryset = TaskModel.objects.filter(is_done=False)
    serializer_class = TaskSerializer

    TO_DO_LIST_ID_URL_KWARG = 'list_id'

    def get_queryset(self):
        return self.queryset.filter(todo_list_id=self.kwargs[self.TO_DO_LIST_ID_URL_KWARG])


class CompletedToDoListTasksAPIView(ListAPIView):  # Deprecated
    queryset = TaskModel.objects.filter(is_done=True)
    serializer_class = TaskSerializer

    TO_DO_LIST_ID_URL_KWARG = 'list_id'

    def get_queryset(self):
        return self.queryset.filter(todo_list_id=self.kwargs[self.TO_DO_LIST_ID_URL_KWARG])


class ToDoListGroupViewSet(viewsets.ModelViewSet):
    queryset = ToDoListGroupModel.objects.all()
    serializer_class = ToDoListGroupModelSerializer


class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoListModel.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ToDoListCreateSerializer
        return ToDoListReadSerializer


@api_view(['GET'])
def todo_list_group_todos(request, todo_list_group_pk=None):
    todo_list_group = ToDoListGroupModel.objects.filter(pk=todo_list_group_pk).first()
    if not todo_list_group:
        logger.error(f'To Do List group with id {todo_list_group_pk} not found')
        return Response(status=HTTP_404_NOT_FOUND)
    logger.info(f'Processing {todo_list_group}')
    serializer = ToDoListReadSerializer(instance=todo_list_group.todo_lists, many=True)
    return Response(serializer.data)
