# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uLogName', models.CharField(max_length=50, verbose_name=b'LogName')),
                ('uPassword', models.CharField(max_length=32, verbose_name=b'Password')),
                ('uFirstName', models.CharField(max_length=50, verbose_name=b'FirstName')),
                ('uLastName', models.CharField(max_length=50, verbose_name=b'LastName')),
                ('uRealName', models.CharField(default=b'', max_length=50, verbose_name=b'RealName', blank=True)),
                ('uSpellName', models.CharField(default=b'', max_length=50, verbose_name=b'SpellName', blank=True)),
                ('uAcronymyName', models.CharField(default=b'', max_length=10, verbose_name=b'AcronymyName', blank=True)),
                ('uIsDel', models.BooleanField(default=False, verbose_name=b'IsDel')),
                ('uIsFirst', models.BooleanField(default=True, verbose_name=b'IsFirst')),
                ('uGroup', models.CharField(default=b'', max_length=50, verbose_name=b'Group', blank=True)),
                ('uThumbnail', models.ImageField(upload_to=b'user', width_field=512, height_field=512, blank=True, verbose_name=b'Thumbnail')),
                ('uThumbnailSmall', models.ImageField(upload_to=b'user', width_field=90, height_field=90, blank=True, verbose_name=b'ThumbnailSmall')),
                ('uEmail', models.EmailField(max_length=254, verbose_name=b'Email', blank=True)),
                ('uPhone', models.CharField(default=b'', max_length=50, verbose_name=b'Phone', blank=True)),
                ('uQQ', models.CharField(default=b'', max_length=50, verbose_name=b'QQ', blank=True)),
                ('uGender', models.CharField(default=b'', max_length=1, verbose_name=b'Gender', blank=True, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('uBirthday', models.DateTimeField(null=True, verbose_name=b'Birthday', blank=True)),
                ('uIdentity', models.CharField(default=b'', max_length=18, verbose_name=b'Identity', blank=True)),
                ('uEntryDate', models.DateTimeField(null=True, verbose_name=b'EntryDate', blank=True)),
                ('uLeaveDate', models.DateTimeField(null=True, verbose_name=b'LeaveDate', blank=True)),
                ('uCreateDate', models.DateTimeField(auto_now_add=True, verbose_name=b'CreateDate')),
                ('uLastModifyData', models.DateTimeField(auto_now=True, verbose_name=b'LastModifyData')),
                ('uDepartment', models.CharField(default=b'', max_length=50, verbose_name=b'Department', blank=True)),
                ('uDuty', models.CharField(default=b' ', max_length=50, verbose_name=b'Duty', blank=True)),
                ('uLevel', models.SmallIntegerField(null=True, verbose_name=b'Level', blank=True)),
                ('uDutyStatus', models.SmallIntegerField(null=True, verbose_name=b'DutyStatus', blank=True)),
                ('uWage', models.IntegerField(null=True, verbose_name=b'Wage', blank=True)),
                ('uRemark', models.TextField(default=b'', verbose_name=b'Remark', blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
