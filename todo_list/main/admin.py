from django.contrib import admin

from . import models


@admin.register(models.TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_filter = ('name', 'owner')
    search_fields = ('name',)


@admin.register(models.ToDoListModel)
class ToDoListModelAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(models.ToDoListGroupModel)
class ToDoListGroupModelAdmin(admin.ModelAdmin):
    search_fields = ('description',)
