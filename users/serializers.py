#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhangle'
# Creat on '15/11/6'

from users.models import Users
from rest_framework import serializers


class UserSerializers(serializers.Serializer):
    # 其中一种写法是将model里边的字段都写一遍，比如：
    # uLogName = serializers.CharField(max_length=50)
    # 以下是简写方式
    class Meta:
        model = Users
        field = ('uLogName',
                 'uPassword',
                 'uIsDel',
                 'uThumbnailSmall',
                 'uThumbnail',
                 'uIsFirst',
                 'uEmail',
                 'uPhone',
                 'uQQ',
                 'uBirthday',
                 'uEntryDate',
                 'uLeaveDate',
                 'uIdentity',
                 'uGender',
                 'uDepartment',
                 'uDuty',
                 'uLevel',
                 'uDutyStatus',
                 'uWage',
                 'uRemark'
                 )

    # 传入instance对象和attrs属性，将attrs属性的值付给instance对象的属性，并且返回
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.uLogName = attrs['uLogName']
            return instance
        return Users(**attrs)