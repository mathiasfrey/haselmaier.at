# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('job_title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'blog_author/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('title_image', models.ImageField(upload_to=b'blog/')),
                ('body', models.TextField()),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(auto_now=True)),
                ('brand', models.CharField(default=b'GR', max_length=2, choices=[(b'GR', b'Group'), (b'TI', b'Tischlerei'), (b'WA', b'Wohn-Art'), (b'LS', b'Leitstellen'), (b'ET', b'E-Technik'), (b'BL', b'Blog'), (b'P8', b'pg8')])),
                ('renderer', models.CharField(default=b'MD', max_length=2, choices=[(b'MD', b'Markdown'), (b'H5', b'HTML5')])),
                ('author', models.ForeignKey(to='haselsite.BlogAuthor')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Blog Entry',
                'verbose_name_plural': 'Blog Entries',
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('image', models.ImageField(upload_to=b'blog/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LeitstellenProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=50)),
                ('start_year', models.CharField(max_length=4)),
                ('end_year', models.CharField(max_length=4, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeitstellenProjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'leitstellen/')),
                ('project', models.ForeignKey(to='haselsite.LeitstellenProject', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.AddField(
            model_name='blogentry',
            name='tags',
            field=models.ManyToManyField(to='haselsite.BlogTag'),
        ),
    ]
