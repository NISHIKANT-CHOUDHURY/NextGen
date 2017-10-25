# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100, choices=[(b'Project', b'Project'), (b'Lab', b'Lab')])),
                ('location', models.CharField(max_length=100, choices=[(b'EC1', b'EC1'), (b'EC2', b'EC2'), (b'EC3', b'EC3'), (b'EC4', b'EC4')])),
                ('tower', models.CharField(max_length=100, choices=[(b'Tower1', b'Tower1'), (b'Tower2', b'Tower2'), (b'Tower3', b'Tower3'), (b'Tower4', b'Tower4')])),
                ('floor', models.CharField(max_length=100, choices=[(b'EC1', b'EC1'), (b'EC2', b'EC2'), (b'EC3', b'EC3'), (b'EC4', b'EC4')])),
                ('wing', models.CharField(max_length=100, choices=[(b'A', b'wing A'), (b'B', b'wing B')])),
            ],
        ),
    ]
