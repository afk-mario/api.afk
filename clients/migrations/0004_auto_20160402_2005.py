# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-02 20:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_compayname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=140)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=140)),
                ('phone', models.CharField(max_length=140, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'ordering': ['phone'],
            },
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['dateCreated']},
        ),
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='phone',
        ),
        migrations.AddField(
            model_name='phone',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
        ),
        migrations.AddField(
            model_name='email',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
        ),
    ]