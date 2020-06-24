# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haselsite', '0006_auto_20200624_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leitstellenproject',
            name='logo',
            field=models.ImageField(default=b'', upload_to=b'leitstellen-images/'),
        ),
    ]
