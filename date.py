#!/usr/bin/env python
#coding=utf-8
'''
@@auther  pdjun\
算当前时间离今年有多少天
'''
import datetime
import sys
def check_cr(datestr):
	if datestr.find('-') > 0: 
		Date = datestr.split('-') ## 如果输入的字符串里面有-就删除-,并把分割开的字符串组成一个列表
	elif datestr.find('/') > 0: 
		Date = datestr.split('/') ## 如果输入的字符串里面有/就删除/
	else :
		Date=False
	return Date	
#获取当前年并格式化时间
def get_year(year):
	jinnian=datetime.datetime(year,1,1,0,0,0)
	return jinnian
#格式化当前时间
def get_now(year):
	jintian=datetime.datetime(year[0],year[1],year[2],0,0,0)
	return jintian

#格式转换为数字类型
def intdate(argv): 
	arg=[]
	try:
		for i in argv:
			arg.append(int(i))
		return arg
	except Exception,e:
		print e
		print "输入有误，请输入数字!"
	
datetime_cr=raw_input('请输入日期 eg 2016-01-01或者2016/01/01 ：')
D=check_cr(datetime_cr)
if D:
	Dd=intdate(D)
	day=(get_now(Dd)-get_year(Dd[0])).days #算出相差多少天
	print day
else:
	print "请输入日期 eg 2016-01-01或者2016/01/01"
