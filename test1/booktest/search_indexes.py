#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件：search_indexes.py
@说明：
@时间：2020/01/01 23:08:28
@作者：MrShiSan
@版本：1.0
@运行环境：Python3.5 + Django1.8.2
'''

from haystack import indexes
from booktest.models import GoodsInfo

''' 创建索引
    1.在你的应用目录下面新建一个search_indexes.py文件，文件名不能修改！
    2.适用：
        数据量非常大的时候，想要快速查找
    3.索引实现的细节并不是我们需要关心的事情，但是它为哪些字段创建索引，怎么指定，下面来说明：
        　每个索引里面必须有且只能有一个字段为 document=Ture，
          这代表着haystack和搜索引擎将使用此字段的内容作为索引进行检索（primary field）
          其他的字段只是附属的属性，方便调用，并不做检索的依据。
        注意：如果一个字段设置了document=True,则一般约定此字段名为text，这是ArticleIndex类里面一贯的写法。
        另外，我们在text字段上提供了use_template=Ture。这允许我们使用一个数据模板，来构建文档搜索引擎索引。
        templates文件夹中建立一个新的模板，search/indexes/项目名/模型名_text.txt，并且将以下的内容放入txt文件中：
            #在目录“templates/search/indexes/应用名称/”下创建“模型类名称_text.txt”文件
            {{ object.title }}
            {{ object.desc }}
            {{ object.content }}
                上面数据模板的作用就是对Note.title, 
                Note.user.get_full_name,Note.body这三个字段建立索引，当检索的时候会对这三个字段做全文检索匹配。

'''


# @note 指定对于某个类的某些数据建立索引
class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return GoodsInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()