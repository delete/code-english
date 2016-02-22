# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 02:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160221_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interests', to=settings.AUTH_USER_MODEL),
        ),
    ]
