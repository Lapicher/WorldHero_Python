# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 20:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('intro', models.CharField(max_length=400)),
                ('body', models.TextField()),
                ('imageUrl', models.URLField()),
                ('datePub', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.Category')),
            ],
        ),
    ]
