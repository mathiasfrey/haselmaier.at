# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import gal.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', unique=True, max_length=250)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('order', models.IntegerField(default=0, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=250, blank=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=gal.models.file_upload)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('order', models.IntegerField(default=0, blank=True)),
                ('category', models.ForeignKey(related_name='pictures', to='gal.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='gallery',
            field=models.ForeignKey(related_name='categories', to='gal.Gallery'),
        ),
    ]
