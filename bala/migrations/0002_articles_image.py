# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-12 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bala', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
