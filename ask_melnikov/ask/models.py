# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import User
from django.db import models


'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.TextField(default="/img/avatar1.png")
    rating = models.IntegerField(default=0)'''


class Profile(models.Model):
    nickname = models.CharField(primary_key=True, max_length=20, default='nick')
    avatar = models.TextField(default="/img/avatar1.png")
    e_mail = models.CharField(max_length=30, default='ad@m.in')
    date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname


class Tag(models.Model):
    title = models.CharField(primary_key=True, max_length=99)

    def __str__(self):
        return self.title


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=99)
    text = models.TextField(default="")
    author = models.ForeignKey(Profile, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0)
    a_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.id) + " / " + str(self.date) + " / " + self.title


class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=128)
    author = models.ForeignKey(Profile, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0)
    quest = models.ForeignKey(Question, null=True)

    def __str__(self):
        return self.text
