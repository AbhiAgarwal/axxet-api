# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150911_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='name',
            field=models.CharField(
                max_length=100,
                null=True,
                blank=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='user',
            field=models.ForeignKey(
                related_name='asset_user',
                verbose_name=b'Owner',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
