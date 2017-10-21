# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-05 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0027_issue_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='label',
            field=models.PositiveSmallIntegerField(
                choices=[(0, b'General'), (1, b'Number Error'), (2, b'Functional'), (3, b'Performance'),
                         (4, b'Security'), (5, b'Typo'), (6, b'Design')], default=0),
        ),
    ]
