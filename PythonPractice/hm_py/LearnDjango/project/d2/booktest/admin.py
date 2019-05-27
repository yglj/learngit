from django.contrib import admin
from booktest.models import *
# Register your models here.


class AreaStackedInline(admin.StackedInline):
    model = AreaInfo
    extra = 1


class AreaTabularInline(admin.TabularInline):
    model = AreaInfo
    extra = 1


@admin.register(AreaInfo)
class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parentNode', 'child', 'parent']
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    list_filter = ['title']  # 右侧过滤器
    search_fields = ['title'] # 搜索框

    # fields = ['parentNode', 'title']  # 字段排序
    fieldsets = (('父地区',{'fields':('parentNode',)}),
                 ('地区',{'fields':('title',)}),
                 )
    inlines = [AreaTabularInline]


admin.site.register(FieldExercise)
# admin.site.register(AreaInfo)
admin.site.register(FileTest)
admin.site.register(HtmlTest)