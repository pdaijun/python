# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointed', '0002_auto_20151222_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='typeId',
            field=models.ForeignKey(to='appointed.UserType'),
        ),
    ]
