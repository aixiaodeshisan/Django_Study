#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :models.py
@说明    :文件跟数据库操作相关,ORM映射操作数据库
@时间    :2019/12/22 16:41:01
@作者    :MrShiSan
@版本    :1.1
'''
from django.db import models

# Create your models here.
''' 入门
'''
# # 图书类
# class BookInfo(models.Model):
#     btitle = models.CharField(max_length = 20)
#     bpub_date = models.DateField()                      # data 型
    
#     # 重写str函数
#     def __str__(self):
#         # 返回书的标题,否则把对象名对象返回
#         return self.btitle

# # 一本书里对应多个英雄，在生成表后，默认会生成一个id对应主键
# class HeroInfo(models.Model):
#     hname = models.CharField(max_length = 20)           # Vchar 型
#     hgender = models.BooleanField()                     # Bool 型
#     hcomment = models.CharField(max_length = 100)
#     hbook = models.ForeignKey("BookInfo")               # 这句代码就让BookInfo类和HeroInfo类之间建立了一对多的关，通过外键联系。

#     def __str__(self):
#         # 返回英雄名
#         return self.hname

''' 模型类扩展
    1.模型实例方法
        str()：在将对象转换成字符串时会被调用。
        save()：将模型对象保存到数据表中，ORM框架会转换成对应的insert或update语句。
        delete()：将模型对象从数据表中删除，ORM框架会转换成对应的delete语句。
    2.模型类的属性
        属性objects：管理器，是models.Manager类型的对象，用于与数据库进行交互。
            默认Django会为每一个模型类生成一个名为objects的管理器
            自定义管理器： books = models.Manager()
    3.管理器Manager
        为啥要自定义管理器：
            1.修改原始查询集，重写all()方法
            2.向管理器类中添加额外的方法，如向数据库中插入数据。
'''

# 图书管理器
class BookInfoManager(models.Manager):
    # 修改原始查询集，重写all()方法。
    def all(self):
        # 默认查询未删除的图书信息
        # 调用父类的成员语法为：super().方法名
        return super().all().filter(isDelete=False)
    
    #创建模型类，接收参数为属性赋值
    def create_book(self, title, pub_date,read,comment):
        #创建模型类对象self.model可以获得模型类
        book = self.model()
        book.btitle = title
        book.bpub_date = pub_date
        book.bread = read
        book.bcomment = comment
        book.isDelete = False
        # 将数据插入进数据表
        book.save()
        return book
    


''' 定义模型类，再数据库中叫实体对像
    1.模型类被定义在"应用/models.py"文件中，此例中为"booktest/models.py"文件。
    2.模型类必须继承自Model类，位于包django.db.models中。
    3.提示：对于重要数据使用逻辑删除。
'''
#定义图书模型类BookInfo
class BookInfo(models.Model):
    ''' 定义模型属性
    django模型的特点：
        django会为表创建自动增长的主键列，每个模型只能有一个主键列，
        如果使用选项设置某属性为主键列后django不会再创建自动增长的主键列。
        默认创建的主键列属性为id，可以使用pk代替，pk全拼为primary key。
    属性命名限制：
        不能是python的保留关键字。
        不允许使用连续的下划线，这是由django的查询方式决定的，在第4节会详细讲解查询。
        定义属性时需要指定字段类型，通过字段类型的参数指定选项
    '''
    # 属性=models.字段类型(选项)
    # 字段类型：
    #   AutoField---自动增长的IntegerField
    #   BooleanField：布尔字段，值为True或False。
    #   NullBooleanField：支持Null、True、False三种值。
    #   CharField(max_length=字符长度)：字符串。
    #   TextField：大文本字段，一般超过4000个字符时使用。
    #   DecimalField(max_digits=None, decimal_places=None)：十进制浮点数。
    #       参数max_digits表示总位数。
    #       参数decimal_places表示小数位数。
    #   FloatField：浮点数。
    #   DateField[auto_now=False, auto_now_add=False])：日期。
    #       参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false。
    #       参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false。
    #       参数auto_now_add和auto_now是相互排斥的，组合将会发生错误。
    #   TimeField：时间，参数同DateField。
    #   DateTimeField：日期时间，参数同DateField。
    #   FileField：上传文件字段。
    #   ImageField：继承于FileField，对上传的内容进行校验，确保是有效的图片。
    btitle = models.CharField(max_length=20,db_column="title")   # 图书名称,指定字段名位title
    bpub_date = models.DateField()                               # 发布日期
    bread = models.IntegerField(default=0)                       # 阅读量
    bcomment = models.IntegerField(default=0)                    # 评论量
    isDelete = models.BooleanField(default=False)                # 逻辑删除
    # 在模型类BookInfo中定义自定义图书管理器
    books = BookInfoManager()

    def __str__(self):
        return self.btitle
    
    ''' 元选项
        1.在模型类中定义类Meta，用于设置元信息，如使用db_table自定义表的名字。
            数据表的默认名称:
                <app_name>_<model_name>
                如：booktest_bookinfo
    '''
    #定义元选项
    class Meta:
      db_table='bookinfo' #指定BookInfo生成的数据表名为bookinfo

''' 逻辑删除
    逻辑删除的本质是修改操作，所谓的逻辑删除其实并不是真正的删除，
    而是在表中将对应的是否删除标识（is_delete）
    或者说是状态字段（status）做修改操作。
    比如False是未删除，True是删除。在逻辑上数据是被删除的，但数据本身依然存在库中。
'''
''' 物理删除
    对应的SQL语句：delete from 表名 where 条件；
    执行该语句，即为将数据库中该信息进行彻底删除，无法恢复。
'''

# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    ''' 选项
        null：如果为True，表示允许为空，默认值是False。
        blank：如果为True，则该字段允许为空白，默认值是False。
        对比：null是数据库范畴的概念，blank是表单验证范畴的。
        db_column：字段的名称，如果未指定，则使用属性的名称。
        db_index：若值为True, 则在表中会为此字段创建索引，默认值是False。
        default：默认值。
        primary_key：若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用。
        unique：如果为True, 这个字段在表中必须有唯一值，默认值是False。
    '''
    hname = models.CharField(max_length=20)                          # 英雄姓名
    hgender = models.BooleanField(default=True)                      # 英雄性别，默认男
    isDelete = models.BooleanField(default=False)                    # 逻辑删除
    hcomment = models.CharField(max_length=200,null=True,blank=False)# 英雄描述信息
    hbook = models.ForeignKey('BookInfo')                            # 英雄与图书表的关系为多对一，所以属性定义在英雄模型类中

    def __str__(self):
        # 返回英雄名
        return self.hname
''' 关系字段类型
    1.关系型数据库的关系包括三种类型：
      ForeignKey：一对多，将字段定义在多的一端中。
      ManyToManyField：多对多，将字段定义在任意一端中。
      OneToOneField：一对一，将字段定义在任意一端中。
      可以维护递归的关联关系，使用'self'指定，详见"自关联"。
    2.一对多关系
      参见booktest应用中的BookInfo类和HeroInfo类。
    3.多对多关系
      新闻类和新闻类型类，一个新闻类型下可以用很多条新闻，一条新闻也可能归属于多种新闻类型。
      新建一个应用newstest,注册应用之后，编辑newstest/models.py文件设计模型类。
'''
''' 自关联
    1.对于地区信息、分类信息等数据，表结构非常类似
      每个表的数据量十分有限，为了充分利用数据表的大量数据存储功能
      可以设计成一张表，内部的关系字段指向本表的主键，这就是自关联的表结构。
'''
# 定义地区模型类，存储省、市、区县信息
class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)                  # 名称
    aParent = models.ForeignKey('self',null=True,blank=True)  # 关系,内部的关系字段指向本表的主键
    pass



