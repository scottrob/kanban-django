# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('damage', models.IntegerField()),
                ('icon', models.CharField(max_length=255)),
                ('rarity', models.CharField(max_length=20)),
            ],
        ),
    ]
