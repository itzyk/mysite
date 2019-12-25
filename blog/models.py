# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ("-publish",)   # 规定了BlogArticles实例对象的显示顺序，即按>照publish字段值的倒序显示

    def __str__(self):
        return self.title

