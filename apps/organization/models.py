from datetime import datetime

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    desc = models.CharField(max_length=200, verbose_name="城市描述")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    category = models.CharField(verbose_name="机构类别", default="pxjg", max_length=20,
                               choices=(("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高校")))
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    course_nums = models.IntegerField(default=0, verbose_name="课程数")
    image = models.ImageField(upload_to='org/%Y/%m', max_length=100, verbose_name="封面图")
    address = models.CharField(max_length=150, verbose_name="机构地址")
    city = models.ForeignKey(City, verbose_name="所在城市", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    #获取机构的老师数
    def get_teacher_nums(self):
        return self.teacher_set.all().count()

    #获取课程数
    def get_course_nums(self):
        return self.course_set.all().count()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="教师名")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    avatar = models.ImageField(default='', upload_to='teacher/%Y/%m', max_length=100, verbose_name="头像")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    #获取讲师所有课程
    def get_teacher_courses(self):
        return self.course_set.all()

    def __str__(self):
        return self.name
