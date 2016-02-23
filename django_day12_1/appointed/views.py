#coding:utf-8
from django.shortcuts import render, render_to_response,redirect
from appointed import models


# Create your views here.

def login(request):    
    ret = {'status':''} 
    #当提交表单的时候获取username和password       
    if request.method == 'POST':
        username = request.POST.get('username',None)        
        password = request.POST.get('password',None)
        is_auth=all([username,password])
        #判断账户和密码是否为空
        if is_auth:
            #过滤数据库当count=1的时候说明账户密码正确
            count=models.UserInfo.objects.filter(username=username,password=password).count()
            if count ==1:
                #跳转到index页面
                return redirect('/appointed/index/')
            else:
                ret['status']='username and password is error'
        else:
            ret['status']='username and password is empty'
    #如果是刷新页面的话 
    return render_to_response('login.html',ret)

def index(request):
    return render_to_response('index.html')
def host(request):
    #定义状态数据和组
    ret ={'status':'','data':None,'group':None}
    #获取组
    usergroup = models.UserGroup.objects.all()
    ret['group']=usergroup
    #添加主机，提交表单
    if request.method=='POST':
        #获取输入的主机名，如果没有则为空
        hostname =request.POST.get('hostname',None)
        #获取输入的IP，如果没有则为空
        ip = request.POST.get('ip',None)
        #获取输入的用户组，如果没有则为空
        groupId = request.POST.get('group',None)
        #判断主机和IP是否输入
        is_auth = all([hostname,ip])
        if is_auth:
            #通过组ID获取外键的对象----->groupobj=UserGroup表的数据(id=groupId)
            groupObj = models.UserGroup.objects.get(id=groupId)
            #向数据库添加数据
            models.Asset.objects.create(hostname=hostname,ip=ip,user_group=groupObj)
        else:
            ret['status']='hostname或ip不能为空'
    #获取Asset表里面的所有数据
    data = models.Asset.objects.all()
    ret['data']=data
    #将数据返回给host.html
   
        #获取ID=2的主机列表
    assetlist=models.Asset.objects.filter(user_group__id=2)
    for item in assetlist:
        print item.hostname
        print item.ip
        print item.user_group.id            
        print item.user_group.GroupName
    
    return render_to_response('host.html',ret)
    
        
        
        