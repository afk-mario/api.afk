# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-03 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20160402_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='currency',
            field=models.CharField(choices=[('MXN', 'MXN'), ('USD', 'USD')], default='MXN', max_length=3),
        ),
    ]