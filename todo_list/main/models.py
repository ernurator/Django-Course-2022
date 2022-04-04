from django.db import models


class ToDoListModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'To Do list'
        verbose_name_plural = 'To Do lists'

    def __str__(self):
        return self.name


class TaskModel(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField()
    due_to = models.DateTimeField()
    owner = models.CharField(max_length=50)  # TODO: change to django user
    is_done = models.BooleanField()
    todo_list = models.ForeignKey(ToDoListModel, models.CASCADE, related_name='tasks')

    class Meta:
        verbose_name = 'To Do task'
        verbose_name_plural = 'To Do tasks'

    def __str__(self):
        return f'{self.name} | {self.created.strftime("%Y-%m-%dT%H:%M:%S")}'
