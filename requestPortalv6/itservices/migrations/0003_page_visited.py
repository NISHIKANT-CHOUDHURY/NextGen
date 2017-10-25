# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itservices', '0002_auto_20170912_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page_visited',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=100)),
                ('desktop_request', models.IntegerField(default=0)),
                ('it_assest_release', models.IntegerField(default=0)),
                ('admin_access', models.IntegerField(default=0)),
                ('software_requestion', models.IntegerField(default=0)),
                ('dns', models.IntegerField(default=0)),
                ('email', models.IntegerField(default=0)),
                ('network', models.IntegerField(default=0)),
                ('it_assest', models.IntegerField(default=0)),
                ('byod', models.IntegerField(default=0)),
                ('link_proposal', models.IntegerField(default=0)),
                ('usb_access', models.IntegerField(default=0)),
            ],
        ),
    ]
