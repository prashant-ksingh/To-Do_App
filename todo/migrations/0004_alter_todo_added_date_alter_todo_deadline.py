# Generated by Django 5.1 on 2024-08-27 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_user_address_alter_todo_added_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 28, 2, 58, 1, 748356)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 28, 2, 58, 1, 748356)),
        ),
    ]
