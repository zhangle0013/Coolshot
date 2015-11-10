# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs_users', '0004_auto_20151109_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ousers',
            name='uThumbnailSmall',
            field=models.ImageField(upload_to=b'user', verbose_name=b'ThumbnailSmall', blank=True),
        ),
    ]
