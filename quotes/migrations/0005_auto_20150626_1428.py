# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_quote_removed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='legacy_hash',
            field=models.CharField(unique=True, editable=False, max_length=42),
        ),
        migrations.AlterField(
            model_name='quote',
            name='text',
            field=models.TextField(),
        ),
    ]
