from django.contrib import admin
from newstest.models import NewsInfo,TypeInfo
# Register your models here.
# 给管理站点注册模型
admin.site.register(TypeInfo)
admin.site.register(NewsInfo)
