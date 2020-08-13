# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haselsite', '0002_leitstellenproject_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='leitstellenproject',
            name='logo',
            field=models.ImageField(default=b'', upload_to=b'leitstellen-images/'),
        ),
        migrations.AlterField(
            model_name='leitstellenproject',
            name='description',
            field=models.TextField(default=b'', max_length=900),
        ),
        migrations.AlterField(
            model_name='leitstellenprojectimage',
            name='image',
            field=models.ImageField(upload_to=b'leitstellen-images/'),
        ),
    ]
