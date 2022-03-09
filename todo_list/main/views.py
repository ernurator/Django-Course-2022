import json

from django.shortcuts import render


def todo_list_view(request):
    with open('./main/todo_list.json', 'r') as f:
        todo_list = json.load(f)
    return render(request, 'todo_list.html', context={'todo_list': todo_list})


def completed_todos_view(request):
    pass
    # return render(request, 'completed_todo_list.jinja')
