# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='level',
            field=models.IntegerField(choices=[(0, 'Basic'), (1, 'Intermediate'), (2, 'Advanced')]),
        ),
    ]
