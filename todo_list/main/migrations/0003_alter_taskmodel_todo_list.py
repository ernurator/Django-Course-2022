# Generated by Django 3.2.12 on 2022-04-04 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220310_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.todolistmodel'),
        ),
    ]
