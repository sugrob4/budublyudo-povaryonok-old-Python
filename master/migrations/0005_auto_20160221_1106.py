# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 09:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_auto_20160221_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата публикации'),
        ),
    ]
