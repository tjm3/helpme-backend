# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 11:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('help_requests', '0002_helprequest_meeting_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpRequestReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='datetime')),
                ('content', models.TextField(verbose_name='content')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='help_request_replies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'help request replies',
                'verbose_name': 'help request reply',
                'ordering': ['datetime'],
            },
        ),
        migrations.AlterField(
            model_name='helprequest',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='help_requests', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='helprequestreply',
            name='help_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='help_request_replies', to='help_requests.HelpRequest'),
        ),
    ]
