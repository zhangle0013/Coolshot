#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'zhangle'
# Creat on '15/11/4'
from django.db import models


# Create your models here.

# 用户数据模型
# 所有模型都继承自models.Model
# blank = True 意思是在验证的时候允许有空值
class Users(models.Model):
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    # 登录名 le.zhang
    uLogName = models.CharField(max_length=50)
    # 密码
    uPassword = models.CharField(max_length=32)
    # 全名，名字完整写法，中文名
    uRealName = models.CharField(max_length=50)
    # 首字母缩写名，在这里指公司人为指定的三个字母名 lez
    uAcronyName = models.CharField(max_length=10)
    # 名字拼写 ZhangLe
    uSpellName = models.CharField(max_length=50)
    # 姓 zhang
    uFirstName = models.CharField(max_length=50)
    # 名 le
    uLastName = models.CharField(max_length=50)
    # 用户是否被删除 true false
    uIsDel = models.BooleanField()
    # 小头像地址，
    uThumbnailSmall = models.ImageField(blank=True, upload_to='user')
    # 大头像地址，FilePathField是用来选择文件的，FileField是上传文件字段
    # ImageField是专用的图像上传字段，依赖python的 Python Imaging Library(PIL)库
    uThumbnail = models.ImageField(blank=True, upload_to='user')
    # 是否第一次登陆？
    uIsFirst = models.BooleanField()
    # 邮箱
    uEmail = models.EmailField(blank=True)
    # 电话
    uPhone = models.CharField(max_length=50, blank=True)
    # QQ号码
    uQQ = models.CharField(max_length=50, blank=True)
    # 生日
    uBirthday = models.DateTimeField(blank=True, null=True)
    # 入职日期
    uEntryDate = models.DateTimeField(blank=True, null=True)
    # 离职日期
    uLeaveDate = models.DateTimeField(blank=True, null=True)
    # 身份证号,比如我的身份证号是18位，有没有更长的号码呢？
    uIdentity = models.CharField(max_length=18, blank=True)
    # 性别
    uGender = models.BooleanField(choices=SEX_CHOICES)
    # 部门  三维，跟踪等
    uDepartment = models.CharField(max_length=50, blank=True)
    # 职位 comp vfx 贴图师，
    uDuty = models.CharField(max_length=50, blank=True)
    # 等级，初级，中级，资深，总监，客户？
    uLevel = models.SmallIntegerField(blank=True)
    # 0：实习；1：试用；2：正式；3：自由职业；4：客户
    uDutyStatus = models.SmallIntegerField(blank=True)
    # 工资,数据类型money
    uWage = models.IntegerField(blank=True)
    # 评论，摘要，附注,无最大值限定
    uRemark = models.TextField(blank=True)
    # 加一个权限组

    def __unicode__(self):
        return self.uLogName


# class Project(models.Model):
#     # 类型
#     pType = models.CharField(max_length=50)
#     # 项目中文名
#     pRealName = models.CharField(max_length=50)
#     # 项目字母全名，拼音或英文
#     pLongName = models.CharField(max_length=50, blank=True)
#     # 项目缩写名  3到4个字母
#     pShortName = models.CharField(max_length=50, blank=True)
#     # ID号，我们自己指定的，4个数字
#     pIdentity = models.IntegerField(blank=True)
#     # 项目全名,包含字母全名、缩写和id
#     pFullName = models.CharField(max_length=50, blank=True)
#     # 项目描述,这个长度可以大一点
#     pDescription = models.CharField(max_length=50, blank=True)
#     # 状态
#     pStatus = models.IntegerField()
#     # 是否删除
#     pIsDel = models.BooleanField()
#     # 颜色 ,这个还不知道给什么数据类型
#     pColor = models.IntegerField()
#     # 负责人 ,不知道什么数据类型
#     pSuperbisor = models.IntegerField(blank=True)
#     # 小缩略图地址
#     pThumbnailSmall = models.FilePathField(blank=True)
#     # 大缩略图地址
#     pThumbnail = models.FilePathField(blank=True)
#     # 项目结束日期
#     pFinalDate = models.DateTimeField(blank=True)
#     # 项目预计开始日期
#     pPreStartDate = models.DateTimeField(blank=True)
#     # 项目预计结束日期
#     pPreEndDate = models.DateTimeField(blank=True)
#     # 项目真正开始日期
#     pStartDate = models.DateTimeField(blank=True)
#     # 项目真正结束日期
#     pEndDate = models.DateTimeField(blank=True)
#     # 评论，摘要，附注,无最大值限定
#     pRemark = models.TextField(blank=True)
#
#     def __unicode__(self):
#         return self.pLongName
#
#
# class Asset(models.Model):
#     aProject = models.IntegerField()
#     aRealName = models.CharField(max_length=50)
#     # tinyint 0:未启动；1：已启动；2：已暂停；3：已取消；4：已完成
#     aStatus = models.IntegerField()
#     aIsDel = models.BooleanField()
#     aSubName = models.CharField(max_length=50, blank=True)
#     aOutRealName = models.CharField(max_length=50, blank=True)
#     aOutSubName = models.CharField(max_length=50, blank=True)
#     # 无最大限定长度
#     aDescription = models.CharField(max_length=50, blank=True)
#     aTags = models.CharField(max_length=36, blank=True)
#     # tinyint
#     aPriority = models.IntegerField(blank=True)
#     # tinyint
#     aComplexity = models.IntegerField(blank=True)
#     # 无最大限定值
#     aPreviewPath = models.CharField(max_length=50, blank=True)
#     aFinalData = models.DateField(blank=True)
#     aPreStartDate = models.DateTimeField(blank=True)
#     aPreEndDate = models.DateTimeField(blank=True)
#     aStartDate = models.DateTimeField(blank=True)
#     aEndDate = models.DateTimeField(blank=True)
#     aSort = models.IntegerField(blank=True)
#     # 评论，摘要，附注,无最大值限定
#     aRemark = models.TextField(max_length=50, blank=True)
#
#     def __unicode__(self):
#         return self.pLongName
#
#
# class Task(models.Model):
#     tProject = models.IntegerField()
#     tIsShot = models.BooleanField()
#     tShot = models.IntegerField(blank=True)
#     tAsset = models.IntegerField(blank=True)
#     tName = models.CharField(max_length=50)
#     # tinyint
#     tProcess = models.IntegerField()
#     # tinyint
#     tTaskStatus = models.IntegerField()
#     # tiniint
#     tStatus = models.IntegerField()
#     tIsDel = models.BooleanField()
#     # 无最大值限定
#     tDescription = models.CharField(max_length=50, blank=True)
#     # tinyint
#     tPriority = models.IntegerField(blank=True)
#     # tinyint
#     tComplexity = models.IntegerField(blank=True)
#     tAssigned = models.IntegerField(blank=True)
#     tSupervisor = models.IntegerField(blank=True)
#     tPreStartDate = models.DateTimeField(blank=True)
#     tPreEndDate = models.DateTimeField(blank=True)
#     # 原来的类型是 decima（18，1）
#     tPreHours = models.DateTimeField(blank=True)
#     tStartDate = models.DateTimeField(blank=True)
#     tEndDate = models.DateTimeField(blank=True)
#     tSort = models.IntegerField(blank=True)
#
#     def __unicode__(self):
#         return self.pLongName
#
#
# class Shot(models.Model):
#     sSequence = models.IntegerField()
#     sCode = models.CharField(max_length=50)
#     # tiny int 0:未启动；1：已启动；2：已暂停；3：已取消；4：已完成
#     sStatus = models.IntegerField()
#     sIsDel = models.BooleanField()
#     sOutCode = models.CharField(max_length=50, blank=True)
#     # 无最大值限定
#     sDescription = models.CharField(max_length=50, blank=True)
#     # 0:单眼；1：双眼
#     sIsStereo = models.BooleanField(blank=True)
#     sIsInFrame = models.IntegerField(blank=True)
#     sStartFrame = models.IntegerField(blank=True)
#     sEndFrame = models.IntegerField(blank=True)
#     sOutFrame = models.IntegerField(blank=True)
#     # 畸变 0：无；1：负；2：正
#     sDistortion = models.BooleanField(blank=True)
#     sFocalLength = models.CharField(max_length=50, blank=True)
#     # tinyint 优先级别
#     sPriority = models.IntegerField(blank=True)
#     # 复杂性 tinyint
#     sComplexity = models.IntegerField(blank=True)
#     # 去畸变后的分辨率
#     sOrthoscopicResolution = models.CharField(max_length=50, blank=True)
#     # 无最大值限定
#     sPreviewPath = models.CharField(max_length=50, blank=True)
#     # 类型 date
#     sFinalDate = models.DateField(blank=True)
#     aPreStartDate = models.DateTimeField(blank=True)
#     aPreEndDate = models.DateTimeField(blank=True)
#     aStartDate = models.DateTimeField(blank=True)
#     aEndDate = models.DateTimeField(blank=True)
#     aSort = models.IntegerField(blank=True)
#     # 评论，摘要，附注,无最大值限定
#     sRemark = models.TextField(blank=True)
#
#     def __unicode__(self):
#         return self.pLongNamepython
#
#
# class Sepuence(models.Model):
#     sqProject = models.IntegerField()
#     sqName = models.CharField(max_length=50)
#     sqIsDel = models.BooleanField()
#     # 无最大值限制
#     sqDescription = models.CharField(max_length=50, blank=True)
#     # 无最大值限制
#     sqPreviewPath = models.CharField(max_length=50, blank=True)
