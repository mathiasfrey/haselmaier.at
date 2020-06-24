# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haselsite', '0003_auto_20200624_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leitstellenprojectimage',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='leitstellenprojectimage',
            name='image2',
            field=models.ImageField(default=b'', upload_to=b'leitstellen-images/', blank=True),
        ),
        migrations.AddField(
            model_name='leitstellenprojectimage',
            name='image3',
            field=models.ImageField(default=b'', upload_to=b'leitstellen-images/', blank=True),
        ),
        migrations.AddField(
            model_name='leitstellenprojectimage',
            name='image4',
            field=models.ImageField(default=b'', upload_to=b'leitstellen-images/', blank=True),
        ),
    ]
