# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0008_auto_20171114_1527'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
    ]
