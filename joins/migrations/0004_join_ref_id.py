# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_join_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default='ABC', max_length=120),
            preserve_default=True,
        ),
    ]
