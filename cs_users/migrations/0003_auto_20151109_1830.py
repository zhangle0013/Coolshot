# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs_users', '0002_auto_20151109_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ousers',
            name='uThumbnail',
            field=models.ImageField(upload_to=b'user', width_field=b'512', height_field=b'512', max_length=200, blank=True, verbose_name=b'Thumbnail'),
        ),
    ]
