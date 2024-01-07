# Generated by Django 5.0.1 on 2024-01-07 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_todo_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
