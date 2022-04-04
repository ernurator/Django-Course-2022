from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToDoListAPIView.as_view()),
    path('<int:list_id>/', views.NotCompletedToDoListTasksAPIView.as_view()),
    path('<int:list_id>/completed/', views.CompletedToDoListTasksAPIView.as_view())
]
