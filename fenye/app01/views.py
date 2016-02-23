#coding:utf-8
from django.shortcuts import render ,render_to_response
from app01 import models

from comm import *
# Create your views here.

def index(request,tag):   
    page=int_page(tag, 1)          
    count_res=models.Host.objects.all().count()      
    Res=INIT_PAGE(page,count_res,)        
    result=models.Host.objects.all()[Res.Start:Res.End] 
    pages=Res.Html_Page()     
    ret={'data':result,'count':count_res,"pagess":pages}  
    return render_to_response('index.html',ret)
