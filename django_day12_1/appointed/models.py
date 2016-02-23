#coding:utf-8
from django.db import models

# Create your models here.
class UserType(models.Model):   
    name = models.CharField(max_length=50) 
class UserInfo(models.Model):
    username= models.CharField(max_length=50)   
    password= models.CharField(max_length=50)
    '''
    Gender = models.BooleanField(default=False)
    Age= models.IntegerField(default=22)
    memo = models.TextField(default='xxxxx')
    create_time=models.DateTimeField(default='2015-10-20 10:20:20')
    '''
    #和UserType做外键，一对多，一个用户一个用户类型，一个用户类型有多个用户
    typeId=models.ForeignKey('userType')
    
class UserGroup(models.Model):
    GroupName = models.CharField(max_length=50)
    #和UserType做外键，多对多，用户可以有多个组，一个组也可以有多个用户
    user = models.ManyToManyField('UserInfo')
'''
class User(models.Model):

    Name = models.CharField(max_length=50)
    Email= models.CharField(max_length=50)
    group_relation = models.ManyToManyField('Group')
'''
class Asset(models.Model):
    hostname=models.CharField(max_length=50)
    creat_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    ip = models.GenericIPAddressField()
    #和用户组做外键，一个主机只存在一个组，一个组有多个主机
    user_group = models.ForeignKey('UserGroup')
    
