# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uLogName', models.CharField(max_length=50)),
                ('uPassword', models.CharField(max_length=32)),
                ('uRealName', models.CharField(max_length=50)),
                ('uAcronyName', models.CharField(max_length=10)),
                ('uSpellName', models.CharField(default=b'', max_length=50, blank=True)),
                ('uFirstName', models.CharField(max_length=50)),
                ('uLastName', models.CharField(max_length=50)),
                ('uIsDel', models.BooleanField(default=False)),
                ('uGroup', models.CharField(default=b'', max_length=50, blank=True)),
                ('uThumbnailSmall', models.ImageField(upload_to=b'user', blank=True)),
                ('uThumbnail', models.ImageField(upload_to=b'user', blank=True)),
                ('uIsFirst', models.BooleanField(default=True)),
                ('uEmail', models.EmailField(max_length=254, blank=True)),
                ('uPhone', models.CharField(default=b'', max_length=50, blank=True)),
                ('uQQ', models.CharField(default=b'', max_length=50, blank=True)),
                ('uBirthday', models.DateTimeField(null=True, blank=True)),
                ('uEntryDate', models.DateTimeField(null=True, blank=True)),
                ('uLeaveDate', models.DateTimeField(null=True, blank=True)),
                ('uIdentity', models.CharField(max_length=18, blank=True)),
                ('uGender', models.CharField(default=b'', max_length=1, blank=True, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('uDepartment', models.CharField(default=b'', max_length=50, blank=True)),
                ('uDuty', models.CharField(default=b' ', max_length=50, blank=True)),
                ('uLevel', models.SmallIntegerField(null=True, blank=True)),
                ('uDutyStatus', models.SmallIntegerField(null=True, blank=True)),
                ('uWage', models.IntegerField(null=True, blank=True)),
                ('uRemark', models.TextField(default=b'', blank=True)),
            ],
        ),
    ]
