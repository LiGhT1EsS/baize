# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 14:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BzArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, unique=True)),
                ('url', models.CharField(max_length=256)),
                ('summary', models.CharField(default='', max_length=512)),
                ('contents', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bz_articles',
            },
        ),
        migrations.CreateModel(
            name='BzLikeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.BigIntegerField(db_index=True)),
                ('user_id', models.BigIntegerField(db_index=True)),
                ('operate', models.SmallIntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bz_like_log',
            },
        ),
        migrations.CreateModel(
            name='BzSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('url', models.CharField(max_length=256, unique=True)),
                ('source_type', models.SmallIntegerField(default=1)),
                ('refresh_freq', models.IntegerField(default=30)),
                ('last_refresh_time', models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 23, 16, 219677))),
                ('author', models.CharField(max_length=64, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bz_source',
            },
        ),
        migrations.AddField(
            model_name='bzarticles',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.BzSource'),
        ),
    ]
