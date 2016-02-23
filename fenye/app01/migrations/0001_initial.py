# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-19 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HostName', models.CharField(max_length=256)),
                ('IP', models.GenericIPAddressField()),
            ],
        ),
    ]
