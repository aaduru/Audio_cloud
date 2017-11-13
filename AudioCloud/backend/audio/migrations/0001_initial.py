# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('track_url', models.CharField(max_length=500)),
                ('image_url', models.CharField(max_length=500)),
                ('artist', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]