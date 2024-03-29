# Generated by Django 5.0.1 on 2024-01-06 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='todo.project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='todo.project')),
            ],
        ),
    ]
