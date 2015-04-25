# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20150425_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='removed',
            field=models.BooleanField(default=False),
        ),
    ]
