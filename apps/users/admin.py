from django.contrib import admin
from users import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.BannerInfo)
admin.site.register(models.EmailVerifyCode)

admin.AdminSite.site_header = '教育项目后台管理系统'
admin.AdminSite.site_title = '教育项目后台管理系统'
