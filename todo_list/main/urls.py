from django.urls import path

from . import views

urlpatterns = [
    path('<int:list_id>/', views.todo_list_view),
    path('<int:list_id>/completed/', views.completed_todos_view)
]
