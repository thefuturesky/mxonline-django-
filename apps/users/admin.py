from django.contrib import admin

# Register your models here.

from .models import UserProfile, EmailVerifyRecord, Banner

admin.site.site_header="慕学在线教育平台管理系统"
admin.site.site_title="慕学在线教育平台"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("nick_name","birday","gender","address","mobile")
    search_fields = ("nick_name","birday","gender","address","mobile")
    list_filter = ('gender', 'address')

class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('email','code', 'send_type', 'send_time')
    search_fields = ("email","send_type","code")
    list_filter = ('send_type', 'send_time')
    date_hierarchy = "send_time"

class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "index", "add_time")
    search_fields = ("title", "index")
    list_filter = ('add_time',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
admin.site.register(Banner, BannerAdmin)
