# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0005_auto_20170525_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='language',
            field=models.CharField(default='en-us', max_length=10),
            preserve_default=False,
        ),
    ]