# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_quote_legacy_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('voter', models.GenericIPAddressField()),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='score',
        ),
        migrations.AddField(
            model_name='vote',
            name='quote',
            field=models.ForeignKey(to='quotes.Quote', related_name='votes'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('voter', 'quote')]),
        ),
    ]
