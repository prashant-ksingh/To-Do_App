# Generated by Django 5.1 on 2024-09-09 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0015_delete_user_todo_user_alter_todo_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 10, 0, 11, 23, 831708)),
        ),
    ]
