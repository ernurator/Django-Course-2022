from django.urls import path

from . import views

urlpatterns = [
    path('', views.todo_list_view),
    path('1/completed/', views.completed_todos_view)
]
