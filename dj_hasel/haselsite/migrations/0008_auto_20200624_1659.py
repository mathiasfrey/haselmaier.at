# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haselsite', '0007_auto_20200624_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leitstellenprojectimage',
            name='project',
        ),
        migrations.DeleteModel(
            name='LeitstellenProjectImage',
        ),
    ]
