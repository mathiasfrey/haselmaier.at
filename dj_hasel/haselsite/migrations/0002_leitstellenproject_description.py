# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haselsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leitstellenproject',
            name='description',
            field=models.TextField(default=b'', max_length=500),
        ),
    ]
