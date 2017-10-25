# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itservices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desktop',
            name='cubical',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desktop',
            name='hard_disk',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desktop',
            name='monitor_size',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desktop',
            name='processor',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desktop',
            name='ram',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='desktop',
            name='floor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='purpose',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='tower',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='wing',
            field=models.CharField(max_length=100),
        ),
    ]
