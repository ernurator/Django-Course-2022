from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register(r'todo_lists', views.ToDoListGroupViewSet, basename='todo-lists-group')
router.register(r'todos', views.ToDoListViewSet, basename='todo-lists-group')

urlpatterns = list(router.urls) + [
    path('todo_lists/<int:todo_list_group_pk>/todos/', views.todo_list_group_todos)
]
