from django.contrib import admin
from operations import models
# Register your models here.

admin.site.register(models.UserAsk)
admin.site.register(models.UserLove)
admin.site.register(models.UserCourse)
admin.site.register(models.UserComment)
admin.site.register(models.UserMessage)