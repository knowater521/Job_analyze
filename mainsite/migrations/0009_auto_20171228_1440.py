# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-28 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_auto_20171228_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='learning',
            name='learnDetail',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='learning',
            name='learnLevel',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='learning',
            name='learnPersons',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
