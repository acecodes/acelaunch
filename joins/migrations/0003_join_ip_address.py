# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0002_auto_20141122_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default='ABC', max_length=120),
            preserve_default=True,
        ),
    ]
