# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-15 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20200415_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='文章内容'),
        ),
    ]
