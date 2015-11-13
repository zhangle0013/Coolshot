#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'zhangle'
# Creat on '15/11/4'
from django.db import models


# Create your models here.

# 用户数据模型
# 所有模型都继承自models.Model
# blank = True 意思是在验证的时候允许有空值
class OUsers(models.Model):
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    # 登录名 le.zhang，必填
    uLogName = models.CharField('LogName', max_length=50)
    # 密码，必填
    uPassword = models.CharField('Password', max_length=32)

    # 名字 zhang,必填，
    uFirstName = models.CharField('FirstName', max_length=50)
    # 姓氏 le，必填，用来生成其他的
    uLastName = models.CharField('LastName', max_length=50)

    # 全名，名字完整写法，中文名，必填，因为习惯不同语言不同，省的造成麻烦,可以为空
    uRealName = models.CharField('RealName', max_length=50, blank=True, default='')
    # 名字拼写 ZhangLe，可以生成，不用必填吧
    uSpellName = models.CharField('SpellName', max_length=50, blank=True, default='')
    # 首字母缩写名，在这里指公司人为指定的三个字母名 lez，必填
    uAcronymyName = models.CharField('AcronymyName', max_length=10, blank=True, default='')

    # 用户是否被删除 true false
    uIsDel = models.BooleanField('IsDel', default=False)
    # 是否第一次登陆？
    uIsFirst = models.BooleanField('IsFirst', default=True)

    # 加一个权限组
    uGroup = models.CharField('Group', max_length=50, blank=True, default='')

    # 大头像地址，FilePathField是用来选择文件的，FileField是上传文件字段
    # ImageField是专用的图像上传字段，依赖python的 Python Imaging Library(PIL)库
    uThumbnail = models.ImageField('Thumbnail', blank=True, upload_to='user', max_length=200)
    # 小头像地址，设置尺寸那个参数需要研究一下怎么用
    uThumbnailSmall = models.ImageField('ThumbnailSmall', blank=True, upload_to='user', max_length=200)

    # 邮箱
    uEmail = models.EmailField('Email', blank=True)
    # 电话
    uPhone = models.CharField('Phone', max_length=50, blank=True, default='')
    # QQ号码
    uQQ = models.CharField('QQ', max_length=50, blank=True, default='')

    # 性别
    uGender = models.CharField('Gender', max_length=1, choices=SEX_CHOICES, blank=True, default='')
    # 生日，用DateField，因为这个值只要精确到天就好了
    uBirthday = models.DateField('Birthday', blank=True, null=True)
    # 身份证号,比如我的身份证号是18位，有没有更长的号码呢？
    uIdentity = models.CharField('Identity', max_length=18, blank=True, default='')

    # 入职日期,用DateField，因为这个值只要精确到天就好了
    uEntryDate = models.DateField('EntryDate', blank=True, null=True)
    # 离职日期，用DateField，因为这个值只要精确到天就好了
    uLeaveDate = models.DateField('LeaveDate', blank=True, null=True)
    # 创建日期
    uCreateDate = models.DateTimeField('CreateDate', auto_now_add=True)
    # 最后编辑日期
    uLastModifyData = models.DateTimeField('LastModifyData', auto_now=True)

    # 部门  三维，跟踪等
    uDepartment = models.CharField('Department', max_length=50, blank=True, default='')
    # 职位 comp vfx 贴图师，
    uDuty = models.CharField('Duty', max_length=50, blank=True, default=' ')
    # 等级，初级，中级，资深，总监，客户？
    uLevel = models.SmallIntegerField('Level', blank=True, null=True)
    # 0：实习；1：试用；2：正式；3：自由职业；4：客户
    uDutyStatus = models.SmallIntegerField('DutyStatus', blank=True, null=True)
    # 工资,数据类型money
    uWage = models.IntegerField('Wage', blank=True, null=True)

    # 评论，摘要，附注,无最大值限定
    uRemark = models.TextField('Remark', blank=True, default='')
    # 加个技能，这样就知道这个人都可以做什么了，有必要么？

    def __unicode__(self):
        return self.uLogName


# class TVersions(models.Model):
#     pass


#
# class TStatus(models.Model):
#     # Ready To Start 准备开始
#     # In Progress 进行中
#     # Awaiting Approval 等待审核
#     # Approved 通过
#     # Unapproved
#     # Final
#     # Omitted
#     # On Hold
#     # Blocked
#     tStatusName = models.CharField(max_length=50)
#     tIcon = models.ImageField(blank=True, max_length=200, upload_to='icon')
#     # 通过这个进度的值，粗略显示一个进度条，可以不同任务的进度做一个加法，看整个镜头的进度
#     tStatusValue = models.IntegerField(blank=True, null=True)
#
#     def __unicode__(self):
#         return self.tStatusName


# 全局的进度状态，连接给资产，项目，场，镜头，Task的进度状态另外写一个。
# 0:未启动；1：已启动；2：已暂停；3：已取消；4：已完成，5：等待准备工作，6：进行中
# class GStatus(models.Model):
#     gStatusName = models.CharField('GlobalStatusName', max_length=50)
#     gStatusDescription = models.TextField('GlobalStatusDescription', blank=True, default='')
#     gStatusOrder = models.IntegerField('GlobalStatusOrder', blank=True, null=True)
#
#     def __unicode__(self):
#         return self.gStatusName

#
# class PProjectType(models.Model):
#     ptName = models.CharField('ProjectTypeName', max_length=50)
#     ptDescription = models.TextField('ProjectTypeDescription', blank=True, default='')
#     ptOrder = models.IntegerField('ProjectTypeOrder', blank=True, null=True)
#
#     def __unicode__(self):
#         return self.ptName


# class PProject(models.Model):
#
#     # 项目字母全名，拼音或英文,最后规范成首字母大写的样子？必填
#     pLongName = models.CharField('LongName', max_length=50, blank=True)
#     # 项目缩写名  3到4个字母。必填
#     pShortName = models.CharField('ShortName', max_length=50, blank=True)
#     # ID号，我们自己指定的，4个数字，必填
#     pIdentity = models.IntegerField('Identity', blank=True)
#     # 项目全名,包含字母全名、缩写和id，这项应该生成
#     pFullName = models.CharField('FullName', max_length=50, blank=True)
#
#     # 类型,连接一个外键吧,多对一连接到PProjectType
#     pType = models.ForeignKey(PProjectType)
#     # 项目中文名
#     pRealName = models.CharField('RealName', max_length=50, blank=True, default='')
#     # 项目描述,这个长度可以大一点
#     pDescription = models.TextField('Description', blank=True, default='')
#     # 状态,也连接一个外键吧，将来可以改,多对一连接到GStatus，全局状态
#     pStatus = models.ForeignKey(GStatus)
#     # 是否删除
#     pIsDel = models.BooleanField('IsDel', default=False)
#     # 颜色 ,这个还不知道给什么数据类型
#     pColor = models.IntegerField('Color', blank=True, null=True)
#
#     # 负责人 ,不知道什么数据类型,连接一个外键
#     pSupervisor = models.IntegerField('Supervisor', blank=True, null=True)
#
#     # 大缩略图地址
#     pThumbnail = models.ImageField('Thumbnail', blank=True, upload_to='project', max_length=200)
#     # 小缩略图地址,小图用大图生成
#     pThumbnailSmall = models.ImageField('ThumbnailSmall', blank=True, upload_to='project', max_length=200)
#
#     # 项目结束日期,精确到天就可以了
#     pFinalDate = models.DateField('FinalDate', blank=True, null=True)
#     # 项目预计开始日期
#     pPreStartDate = models.DateField('PreStartDate', blank=True, null=True)
#     # 项目预计结束日期
#     pPreEndDate = models.DateField('PreEndDate', blank=True, null=True)
#     # 项目真正开始日期
#     pStartDate = models.DateField('StartDate', blank=True, null=True)
#     # 项目真正结束日期
#     pEndDate = models.DateField('EndDate', blank=True, null=True)
#     # 创建日期
#     pCreateDate = models.DateTimeField('CreateDate', auto_now_add=True)
#     # 最后编辑日期
#     pLastModifyData = models.DateTimeField('LastModifyData', auto_now=True)
#
#     # 评论，摘要，附注,无最大值限定
#     pRemark = models.TextField('Remark', blank=True, default='')
#
#     def __unicode__(self):
#         return self.pLongName


# class PAsset(models.Model):
#     # 真实名字，可以是人读懂的名字，中文之类，必填
#     aRealName = models.CharField(max_length=50)
#     # tinyint 0:未启动；1：已启动；2：已暂停；3：已取消；4：已完成,连接到全局状态
#     aStatus = models.ForeignKey(GStatus)
#     # 是否删除
#     aIsDel = models.BooleanField(default=False)
#     # 我觉得这个将来可以连接到很多项目里，所以他可能是一个到Project的多对多连接
#     aProject = models.IntegerField(blank=True, null=True)
#     # 这个必须是将来可以用到标准路径里的名字，英文，拼音，数字，可以带中划线，不要带下划线，必填
#     aSubName = models.CharField(max_length=50)
#     # 假如连接到别的项目，可以让别的项目用下边这两个名字
#     aOutRealName = models.CharField(max_length=50, blank=True, default='')
#     aOutSubName = models.CharField(max_length=50, blank=True, default='')
#     # 无最大限定长度,描述
#     aDescription = models.TextField(blank=True, default='')
#     # 标签，应该是外键
#     aTags = models.CharField(max_length=36, blank=True, default='')
#     # tinyint,优先级,
#     aPriority = models.IntegerField(blank=True, null=True)
#     # tinyint,难度
#     aComplexity = models.IntegerField(blank=True, null=True)
#     # 无最大限定值,缩略图路径
#     aPreviewPath = models.ImageField(max_length=200, blank=True, upload_to='asset')
#     # 完成日期,精确到天就可以了
#     aFinalData = models.DateField(blank=True, null=True)
#     aPreStartDate = models.DateField(blank=True, null=True)
#     aPreEndDate = models.DateField(blank=True, null=True)
#     aStartDate = models.DateField(blank=True, null=True)
#     aEndDate = models.DateField(blank=True, null=True)
#     # 创建日期
#     aCreateDate = models.DateTimeField('CreateDate', auto_now_add=True)
#     # 最后编辑日期
#     aLastModifyData = models.DateTimeField('LastModifyData', auto_now=True)
#     # 这个可能是排序用的？
#     aSort = models.IntegerField(blank=True, null=True)
#     # 评论，摘要，附注,无最大值限定
#     aRemark = models.TextField(blank=True, default='')
#
#     def __unicode__(self):
#         return self.aSubName


# 前期拍摄的记录信息，可以从这里连接到镜头，也可以从镜头创建一条记录,这个系统挺庞大的，完全可以单列一个app
class SShotInformation(models.Model):
    pass


# class PTask(models.Model):
#     # 输入输出也算一个部门
#     # 属于哪个项目,如果属于资产的话，这个可以不写
#     # 应该是项目和资产单选一个，应该在逻辑代码里实现这个,应该是在什么界面点出来，自动获取这前几行信息
#     tProject = models.IntegerField(max_length=50, blank=True, default='')
#     tAsset = models.IntegerField(blank=True, null=True)
#     # 是否属于一个镜头
#     tIsShot = models.BooleanField()
#     # 如果属于镜头，是哪个镜头
#     tShot = models.IntegerField(blank=True)
#     # 任务的名字，应该有2d和3d的任务之分。我觉得这里也应该有逻辑判断
#     # 在什么界面点出啦的，连接到不同的选项
#     # 这个名字应该做个外键，分2d任务和3d任务
#     # 仔细想想，应该不用硬性分开，只是显示的时候有所区别就可以，因为在一个镜头上建立任务的时候，不分3d和2d
#     tName = models.CharField(max_length=50)
#     # tinyint
#     tProcess = models.IntegerField()
#     # tinyint，这个做个外键，专门定义各种状态
#     tTaskStatus = models.ForeignKey(TStatus)
#     # tiniint，连接到全局状态
#     tStatus = models.ForeignKey(GStatus)
#     # 是否删除
#     tIsDel = models.BooleanField(default=False)
#     # 无最大值限定，对这个任务的描述，要求
#     tDescription = models.TextField(blank=True, default='')
#     # tinyint,优先级,应该限定个范围，1-10吧
#     tPriority = models.IntegerField(blank=True, null=True)
#     # tinyint，难度
#     tComplexity = models.IntegerField(blank=True, null=True)
#     # 将任务分配给谁，应该是个外键，连接到User，多对多的关系，判断是那种类型的任务，优先显示这个类型的人
#     tAssigned = models.ManyToManyField(OUsers)
#     # 应该也是个外键，应该连接到一个组（总监组）的其中的一个用户，多对多
#     # 这个严格讲应该叫负责人，不是传统意义上的总监，应该是组长一级的人
#     tSupervisor = models.ManyToManyField(OUsers)
#     # 这个任务的版本，有很多任务，每个任务有很多版本，应该是多对多的关系
#     tVersions = models.ManyToManyField(TVersions)
#
#     # 原来的类型是 decima（18，1），下边的是否可以精确到小时之类的，将来用甘特图来控制时间
#     tPreHours = models.DateTimeField(blank=True, null=True)
#     tPreStartDate = models.DateField(blank=True, null=True)
#     tPreEndDate = models.DateField(blank=True, null=True)
#     tStartDate = models.DateField(blank=True, null=True)
#     tEndDate = models.DateField(blank=True, null=True)
#     tSort = models.IntegerField(blank=True, null=True)
#     # 加个耗时，就是自打任务开始到结束用了多长时间，不是很准的那种
#     # 加个实际耗时，通过timelog记录，比较准确那种。
#     # 加个附件，可以是各种文件，用来指导制作，比如画过的图片
#     tAttachments = models.CharField(blank=True, default='')
#
#     def __unicode__(self):
#         return self.tName


# class PSequence(models.Model):
#     # 属于哪个项目
#     sqProject = models.ForeignKey(PProject, related_name='PSequence')
#     # 必填
#     sqName = models.CharField(max_length=50)
#     sqIsDel = models.BooleanField(default=False)
#     # 无最大值限制
#     sqDescription = models.TextField(blank=True, default='')
#     # 无最大值限制,这个是什么，序列没有预览啊，可能是个视频文件小样
#     sqPreviewPath = models.CharField(max_length=50, blank=True, default='')


# class PShot(models.Model):
#     # 属于哪个序列/场，应该是个外键，应该是必填
#     sSequence = models.ForeignKey(PSequence)
#     # 镜头号，必填
#     sCode = models.CharField(max_length=50)
#     # tiny int 0:未启动；1：已启动；2：已暂停；3：已取消；4：已完成，连接到全局
#     sStatus = models.ForeignKey(GStatus)
#     # 小状态,外键，小状态改变的时候要问一下是否改变镜头状态
#     sShotStatus = models.ForeignKey(TStatus)
#     # 是否删除,这个是不是要和删除状态关联？
#     sIsDel = models.BooleanField(default=False)
#     # 外界的镜头号，就是客户那边的镜头号，用以恢复客户那边的命名
#     sOutCode = models.CharField(max_length=50, blank=True, default='')
#     # 无最大值限定
#     sDescription = models.TextField(blank=True, default='')
#     # 加一个前期记录的详细信息的外键，多个镜头可能对应一个记录，所以是多对一的外键
#     sShootingInfo = models.ForeignKey(SShotInformation)
#     # 0:单眼；1：双眼
#     sIsStereo = models.NullBooleanField(blank=True, null=True)
#     sIsInFrame = models.IntegerField(blank=True, null=True)
#     sStartFrame = models.IntegerField(blank=True, null=True)
#     sEndFrame = models.IntegerField(blank=True, null=True)
#     sOutFrame = models.IntegerField(blank=True, null=True)
#     # 畸变 0：无；1：负；2：正
#     sDistortion = models.NullBooleanField(blank=True, null=True)
#     sFocalLength = models.CharField(max_length=50, blank=True, default='')
#     # tinyint 优先级别
#     sPriority = models.IntegerField(blank=True, null=True)
#     # 复杂性 tinyint
#     sComplexity = models.IntegerField(blank=True, null=True)
#     # 去畸变后的分辨率
#     sOrthoscopicResolution = models.CharField(max_length=50, blank=True, default='')
#     # 无最大值限定
#     sPreviewPath = models.CharField(max_length=50, blank=True, default='')
#     # 类型 date
#     sFinalDate = models.DateField(blank=True, null=True)
#     aPreStartDate = models.DateTimeField(blank=True, null=True)
#     aPreEndDate = models.DateTimeField(blank=True, null=True)
#     aStartDate = models.DateTimeField(blank=True, null=True)
#     aEndDate = models.DateTimeField(blank=True, null=True)
#     aSort = models.IntegerField(blank=True, null=True)
#     # 素材路径，可能是多条，应该连接到一个版本
#     sElementPath = models.ManyToManyField(TVersions)
#     # 参考路径,这个只是个字段而已，用来提醒将来加个东西在这，可以将参考连接到这里，以后再细想吧
#     sReferencePath = models.CharField(max_length=200, blank=True, default='')
#     # 评论，摘要，附注,无最大值限定
#     sRemark = models.TextField(blank=True)
#
#     def __unicode__(self):
#         return self.sCode








