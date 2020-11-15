from django.contrib import admin
from courses import models
# Register your models here.

admin.site.register(models.CourseInfo)
admin.site.register(models.LessonInfo)
admin.site.register(models.VideoInfo)
admin.site.register(models.SourceInfo)