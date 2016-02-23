# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('GroupName', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='group_relation',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='memo',
        ),
        migrations.AddField(
            model_name='asset',
            name='ip',
            field=models.IPAddressField(default='10.203.0.12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='typeId',
            field=models.ForeignKey(to='appointed.UserType'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='usergroup',
            name='user',
            field=models.ManyToManyField(to='appointed.UserInfo'),
        ),
        migrations.AddField(
            model_name='asset',
            name='user_group',
            field=models.ForeignKey(default=1, to='appointed.UserGroup'),
            preserve_default=False,
        ),
    ]
