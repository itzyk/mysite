# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')   # 展示内容
    list_filter = ('publish', 'author')             # 筛选条件
    search_fields = ('title', 'body')               # 搜索
    raw_id_fields = ('author', )                    # 显示外键的详细信息
    date_hierarchy = 'publish'                      # 详细时间分层筛选
    ordering = ['publish', 'author']                # 排序


admin.site.register(BlogArticles, BlogArticlesAdmin)
