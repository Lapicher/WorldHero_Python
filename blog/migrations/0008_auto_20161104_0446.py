# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-04 04:46
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='uploads'),
        ),
    ]