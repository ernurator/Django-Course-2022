from django.db import models


class ToDoListGroupModel(models.Model):
    description = models.CharField(max_length=500)

    @property
    def short_description(self):
        if len(self.description) <= 50:
            return self.description
        return self.description[:47] + '...'

    def __str__(self):
        return f'To Do List Group #{self.id} - {self.short_description}'


class ToDoListModel(models.Model):
    name = models.CharField(max_length=50)
    todo_list_group = models.ForeignKey(ToDoListGroupModel, models.CASCADE, related_name='todo_lists')

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
    image = models.ImageField(null=True)
    todo_list = models.ForeignKey(ToDoListModel, models.CASCADE, related_name='tasks')

    class Meta:
        verbose_name = 'To Do task'
        verbose_name_plural = 'To Do tasks'

    def __str__(self):
        return f'{self.name} | {self.created.strftime("%Y-%m-%dT%H:%M:%S")}'
