# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-17 01:48
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0038_issue_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='issue',
            name='upvoted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='upvoted', to=settings.AUTH_USER_MODEL),
        ),
    ]
