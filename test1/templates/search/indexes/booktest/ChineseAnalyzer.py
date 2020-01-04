#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件：ChineseAnalyzer.py
@说明：
@时间：2020/01/01 23:15:41
@作者：MrShiSan
@版本：1.0
@运行环境：Python3.5 + Django1.8.2
'''

# @note 使用jieba分词
# @note 建立ChineseAnalyzer.py文件
# @note 保存在haystack的安装文件夹下，路径如“D:\python3\Lib\site-packages\haystack\backends”

import jieba
from whoosh.analysis import Tokenizer, Token

class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        t = Token(positions, chars, removestops=removestops, mode=mode,
                  **kwargs)
        seglist = jieba.cut(value, cut_all=True)
        for w in seglist:
            t.original = t.text = w
            t.boost = 1.0
            if positions:
                t.pos = start_pos + value.find(w)
            if chars:
                t.startchar = start_char + value.find(w)
                t.endchar = start_char + value.find(w) + len(w)
            yield t

def ChineseAnalyzer():
    return ChineseTokenizer()