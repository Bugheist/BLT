# Generated by Django 2.0.3 on 2018-06-05 09:27

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0045_auto_20180314_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='email_event',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='webshot',
            field=models.ImageField(blank=True, null=True, upload_to='webshots'),
        ),
        migrations.AlterField(
            model_name='hunt',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='github_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='label',
            field=models.PositiveSmallIntegerField(choices=[(0, 'General'), (1, 'Number Error'), (2, 'Functional'), (3, 'Performance'), (4, 'Security'), (5, 'Typo'), (6, 'Design')], default=0),
        ),
        migrations.AlterField(
            model_name='issue',
            name='ocr',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='screenshot',
            field=models.ImageField(upload_to='screenshots', validators=[website.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(blank=True, default='open', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='user_agent',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.IntegerField(choices=[(0, 'Unrated'), (1, 'Bronze'), (2, 'Silver'), (3, 'Gold'), (4, 'Platinum')], default=0),
        ),
    ]
