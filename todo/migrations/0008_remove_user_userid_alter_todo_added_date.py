# Generated by Django 5.1 on 2024-09-06 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_todo_added_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userid',
        ),
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 2, 33, 46, 700950)),
        ),
    ]