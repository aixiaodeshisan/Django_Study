#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :admin.py
@说明    :跟网站的后台管理相关
@时间    :2019/12/22 16:42:18
@作者    :MrShiSan 
@版本    :1.0
'''

from django.contrib import admin
from booktest.models import *

# @note 自定义管理页面的功能，比如列表页要显示哪些值。
# @note 默认在列表页只显示出了BookInfo object，对象的其它属性并没有列出来，查看非常不方便
class BookInfoAdmin(admin.ModelAdmin):
    # 定义清单中要显示,注要在下面注册本类
    list_display = ['id','btitle','bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcomment','hbook']
''' @todo 控制管理页展示
    1.类ModelAdmin可以控制模型在Admin界面中的展示方式
        主要包括在列表页的展示方式、添加修改页的展示方式
    2.管理类有两种使用方式：
        注册参数
        装饰器
'''
# @audit-ok 关联对象，子类StackedInline，在1以块的形式开始显示多，当选中ID进行所有字段的查看时会显示
class AreaStackedInline(admin.StackedInline):
    model = AreaInfo            # 关联子对象
    extra = 2                   # 额外编辑2个子对象

# @audit-ok 关联对象，用表格的形式嵌入
class AreaTabularInline(admin.TabularInline):
    model = AreaInfo        # 关联子对象
    extra = 2               # 额外编辑2个子对象

# @note 通过修饰器对AreaInfo model进行注册
@admin.register(AreaInfo)
class AreaInfoAdmin(admin.ModelAdmin):
    ''' @note django管理员控制管理，列表页选项（变量名都是定死的）
        1.页大小
            每页中显示多少条数据，默认为每页显示100条数据
            list_per_page=100
        2."操作选项"的位置
            顶部显示的属性，设置为True在顶部显示，默认True
            actions_on_top=True
            底部显示的属性，设置为True在底部显示，默认为False。
            actions_on_bottom=False
            可以两个同时显示
        3.列表中的列列操作
            列显示
                list_display=[模型字段1,模型字段2,...]
                点击列头可以进行升序或降序排列。
                list_displa还可以将方法作为列
                        列可以是模型字段，还可以是模型方法，要求方法有返回值。
                        但是方法列是不能排序的，如果需要排序需要为方法指定排序依据。
                            admin_order_field=模型类字段
            列标题
                列标题默认为属性或方法的名称，可以通过属性设置
                需要先将模型字段封装成方法，再对方法使用short_description这个属性，模型字段不能直接使用这个属性。
                    short_description='列标题'
            关联对象
                无法直接访问关联对象的属性或方法，可以在模型类中封装方法，访问关联对象的成员。
        4.右侧栏过滤器
            属性如下，只能接收字段，会将对应字段的值列出来，用于快速过滤。一般用于有重复值的字段。
        5.搜索框
            用于对指定字段的值进行搜索，支持模糊查询。列表类型，表示在这些字段上进行搜索。
                search_fields=[]
        6.中文标题
            1）打开booktest/models.py文件，修改模型类，为属性指定verbose_name参数，即第一个参数
    '''
    # @audit-ok 显示页多少
    list_per_page = 20
    # @audit-ok 显示"操作选项"的位置
    actions_on_top = True
    actions_on_bottom = True
    # @audit-ok 显示列表中的列,不仅模型的字段可以，而且具有特殊意义的方法也可以通过列表显示，检称方法列
    list_display = ['id','atitle','title','parent']
    # @audit-ok 右侧栏过滤器启用，用于快速过滤
    list_filter=['atitle']
    # @audit-ok 对标题启用搜索框
    search_fields=['atitle']
    
    ''' @note 编辑页选项
        1.显示字段顺序
            fields=['aParent','atitle']
        2.分组显示
            fieldset=(
                ('组1标题',{'fields':('字段1','字段2')}),
                ('组2标题',{'fields':('字段3','字段4')}),
            )
                注意：fields与fieldsets两者选一使用。
        3.关联对象
            在一对多的关系中，可以在一端的编辑页面 中 编辑多端的对象，嵌入多端对象的方式包括表格、块两种。
            类型InlineModelAdmin：表示在模型的编辑页面嵌入关联模型的编辑。
            子类TabularInline：以表格的形式嵌入。
            子类StackedInline：以块的形式嵌入。
    '''
    # @audit-ok 显示字段顺序,选中ID后就会显示字段，以自定义顺序展示
    # fields=['aParent','atitle']
    # @audit-ok 将字段进行分组显示，fieldsets 和 fields 只能存在一个
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )
    # @audit-ok 调用块形式显示多的一方
    inlines = [AreaStackedInline]
    # @audit-ok 调用表格形式显示多的一方
    # inlines = [AreaTabularInline]
    ''' @todo 重写django html 布局模板
        1.在templates/目录下创建admin目录
        2.打开当前虚拟环境中Django的目录，再向下找到admin的模板(需要在django库里面找，然后复制粘贴过来更改)
            /home/python/.virtualenvs/py_django/lib/python3.5/site-packages/django/contrib/admin/templates/admin
            A:\MyApply\Soft\CodeApply\Python\virtualenv\py35_django1.8.2\Lib\site-packages\django\contrib\admin\templates\admin
        3.将需要更改文件拷贝到第一步建好的目录里，此处以base_site.html为例
    '''
# @note 富文本编辑器tinymce的使用
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id']



# Register your models here.
# @todo 注意想要在站点里面显示的相关实体，都必须在这注册才会显示
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
# @note 通过注册参数方式对AreaInfo model进行注册，还可采用修饰器
# admin.site.register(AreaInfo,AreaInfoAdmin)
# @audit-ok 在管理员页面注册上传图片
admin.site.register(PicTest)
admin.site.register(GoodsInfo,GoodsInfoAdmin)