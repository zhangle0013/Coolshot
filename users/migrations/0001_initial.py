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
                ('uSpellName', models.CharField(max_length=50)),
                ('uFirstName', models.CharField(max_length=50)),
                ('uLastName', models.CharField(max_length=50)),
                ('uIsDel', models.BooleanField()),
                ('uThumbnailSmall', models.ImageField(upload_to=b'user', blank=True)),
                ('uThumbnail', models.ImageField(upload_to=b'user', blank=True)),
                ('uIsFirst', models.BooleanField()),
                ('uEmail', models.EmailField(max_length=254, blank=True)),
                ('uPhone', models.CharField(max_length=50, blank=True)),
                ('uQQ', models.CharField(max_length=50, blank=True)),
                ('uBirthday', models.DateTimeField(null=True, blank=True)),
                ('uEntryDate', models.DateTimeField(null=True, blank=True)),
                ('uLeaveDate', models.DateTimeField(null=True, blank=True)),
                ('uIdentity', models.CharField(max_length=18, blank=True)),
                ('uGender', models.BooleanField(choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('uDepartment', models.CharField(max_length=50, blank=True)),
                ('uDuty', models.CharField(max_length=50, blank=True)),
                ('uLevel', models.SmallIntegerField(blank=True)),
                ('uDutyStatus', models.SmallIntegerField(blank=True)),
                ('uWage', models.IntegerField(blank=True)),
                ('uRemark', models.TextField(blank=True)),
            ],
        ),
    ]
