# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 11:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20190326_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
