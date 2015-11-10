# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs_users', '0003_auto_20151109_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ousers',
            name='uThumbnail',
            field=models.ImageField(upload_to=b'user', max_length=200, verbose_name=b'Thumbnail', blank=True),
        ),
    ]
