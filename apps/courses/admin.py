from django.contrib import admin

# Register your models here.

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time')
    search_fields = ("name", "degree", "learn_times", 'students', 'fav_nums', 'click_nums')
    list_filter = ('degree', 'students', 'learn_times', 'fav_nums', 'click_nums', 'add_time')
    date_hierarchy = "add_time"


class LessonAdmin(admin.ModelAdmin):
    list_display = ("course", "name", "add_time")
    search_fields = ("course", "name")
    list_filter = ('course', "add_time")


class VideoAdmin(admin.ModelAdmin):
    list_display = ("lesson", "name", "add_time")
    search_fields = ("lesson", "name")
    list_filter = ('lesson', "add_time")


class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ("course", "name", "add_time")
    search_fields = ("course", "name")
    list_filter = ('course', "add_time")


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(CourseResource, CourseResourceAdmin)
