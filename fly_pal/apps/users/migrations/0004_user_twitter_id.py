# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151108_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='twitter_id',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
