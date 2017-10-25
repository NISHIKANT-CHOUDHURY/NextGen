# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itservices', '0004_auto_20171017_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desktop',
            old_name='city',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='desktop',
            old_name='cubical',
            new_name='days',
        ),
        migrations.RenameField(
            model_name='desktop',
            old_name='floor',
            new_name='laptop_type',
        ),
        migrations.RemoveField(
            model_name='desktop',
            name='hard_disk',
        ),
        migrations.RemoveField(
            model_name='desktop',
            name='monitor_size',
        ),
        migrations.RemoveField(
            model_name='desktop',
            name='processor',
        ),
        migrations.RemoveField(
            model_name='desktop',
            name='purpose',
        ),
        migrations.RemoveField(
            model_name='desktop',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='desktop',
            name='tower',
        ),
        migrations.RemoveField(
            model_name='desktop',
            name='wing',
        ),
    ]
