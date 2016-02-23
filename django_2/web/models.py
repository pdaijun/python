from django.db import models



# Create your models here.

    
class userType(models.Model):   
    name = models.CharField(max_length=50) 
class UserInfo(models.Model):
    username= models.CharField(max_length=50)   
    password= models.CharField(max_length=50)
    Gender = models.BooleanField(default=False)
    Age= models.IntegerField(default=22)
    memo = models.TextField(default='xxxxx')
    create_time=models.DateTimeField(default='2015-10-20 10:20:20')
    typeId=models.ForeignKey('userType')
    
class Group(models.Model):
    Name = models.CharField(max_length=50)
class User(models.Model):
    Name = models.CharField(max_length=50)
    Email= models.CharField(max_length=50)
    group_relation = models.ManyToManyField('Group')
class Asset(models.Model):
    hostname=models.CharField(max_length=50)
    creat_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    
