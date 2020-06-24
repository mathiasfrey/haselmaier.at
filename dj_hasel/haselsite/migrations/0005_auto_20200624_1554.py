# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haselsite', '0004_auto_20200624_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='leitstellenproject',
            name='image1',
            field=models.ImageField(default=b'', upload_to=b'leitstellen-images/', blank=True),
        ),
        migrations.AddField(
            model_name='leitstellenproject',
            name='image2',
            field=models.ImageField(default=b'', upload_to=b'leitstellen-images/', blank=True),
        ),
        migrations.AddField(
            model_name='leitstellenproject',
            name='image3',
            field=models.ImageField(default=b'', upload_to=b'leitstellen-images/', blank=True),
        ),
    ]
