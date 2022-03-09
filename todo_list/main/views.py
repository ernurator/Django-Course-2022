from django.shortcuts import render
from django.template import Context


# Create your views here.
def todo_list_view(request):
    return render(request, 'todo_list.html', context={'title': 'some test title'})


def completed_todos_view(request):
    pass
    # return render(request, 'completed_todo_list.jinja')
