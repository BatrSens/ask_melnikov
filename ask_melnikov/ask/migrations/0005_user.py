# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0004_auto_20171114_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=99)),
                ('text', models.TextField(default='')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('a_count', models.IntegerField(default=0)),
            ],
        ),
    ]
