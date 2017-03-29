# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import todo.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Créé le')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modifié le')),
                ('name', models.CharField(max_length=60, verbose_name='Nom du groupe')),
                ('avatar', models.ImageField(upload_to=todo.models.avatar_filename, blank=True, verbose_name='Avatar Groupe', null=True, validators=[todo.models.validate_image])),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('avatar', models.ImageField(upload_to=todo.models.avatar_filename, blank=True, verbose_name='Avatar membre', null=True, validators=[todo.models.validate_image])),
            ],
            options={
                'ordering': ['user__date_joined'],
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Créé le')),
                ('type', models.CharField(choices=[('developper', 'Développeur'), ('guest', 'Invité'), ('manager', 'Manager')], default='guest', max_length=15, verbose_name='Type de relation ')),
                ('group', models.ForeignKey(to='todo.Group')),
                ('member', models.ForeignKey(to='todo.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Créé le')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modifié le')),
                ('notify_mail', models.BooleanField(default=True, verbose_name='Notification par Email ? ')),
                ('notify_sms', models.BooleanField(default=True, verbose_name='Notification par SMS ? ')),
                ('created_by', models.ForeignKey(related_name='todo_setting_creator', verbose_name='Créé par', to='todo.Member')),
                ('modified_by', models.ForeignKey(related_name='todo_setting_modificator', verbose_name='Modifié par', to='todo.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Créé le')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modifié le')),
                ('name', models.CharField(max_length=60, verbose_name='Nom')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('due_date', models.DateTimeField(blank=True, null=True, default=datetime.datetime(2017, 3, 29, 14, 13, 26, 328325, tzinfo=utc), verbose_name='Fin prévue le')),
                ('completed', models.BooleanField(default=False, verbose_name='Tache terminée ? ')),
                ('status', models.CharField(choices=[(None, '---')], blank=True, null=True, default=None, max_length=20)),
                ('created_by', models.ForeignKey(related_name='todo_task_creator', verbose_name='Créé par', to='todo.Member')),
                ('modified_by', models.ForeignKey(related_name='todo_task_modificator', verbose_name='Modifié par', to='todo.Member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='settings',
            field=models.ForeignKey(blank=True, verbose_name='Paramêtres', null=True, to='todo.Setting'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(related_name='todo_group_creator', verbose_name='Créé par', to='todo.Member'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='groups', through='todo.Relation', verbose_name='Membre du groupe', to='todo.Member'),
        ),
        migrations.AddField(
            model_name='group',
            name='modified_by',
            field=models.ForeignKey(related_name='todo_group_modificator', verbose_name='Modifié par', to='todo.Member'),
        ),
        migrations.AddField(
            model_name='group',
            name='settings',
            field=models.ForeignKey(verbose_name='Paramêtres', to='todo.Setting'),
        ),
    ]
