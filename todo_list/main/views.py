import json

from django.shortcuts import render


def get_todo_list_items(get_done_items=False):
    with open('./main/todo_list.json', 'r') as f:
        items = [item for item in json.load(f) if item['done'] is get_done_items]
    return items


def todo_list_view(request):
    todo_list_items = get_todo_list_items()
    return render(request, 'todo_list.html', context={'todo_list': todo_list_items})


def completed_todos_view(request):
    todo_list_items = get_todo_list_items(get_done_items=True)
    return render(request, 'completed_todo_list.html', context={'todo_list': todo_list_items})
