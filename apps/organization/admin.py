from django.contrib import admin

# Register your models here.

from .models import City, CourseOrg, Teacher


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "add_time")
    search_fields = ("name", "desc")
    list_filter = ("desc", "add_time")


class CourseOrgAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "click_nums", 'fav_nums', 'address', 'city', 'add_time')
    search_fields = ("name", "desc", "click_nums", 'fav_nums', 'address', 'city')
    list_filter = ("click_nums", 'fav_nums', 'address', 'city', 'add_time')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", 'org', 'work_years', "work_company", 'work_position', 'points', 'click_nums', 'fav_nums', "add_time")
    search_fields = ("name", 'org', 'work_years', "work_company", 'work_position', 'points', 'click_nums', 'fav_nums')
    list_filter = ('org', 'work_years', "work_company", 'work_position' , 'click_nums', 'fav_nums', "add_time")


admin.site.register(City, CityAdmin)
admin.site.register(CourseOrg, CourseOrgAdmin)
admin.site.register(Teacher, TeacherAdmin)
