# Generated by Django 3.2.4 on 2021-07-31 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_todo_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='ip',
            new_name='email',
        ),
    ]
