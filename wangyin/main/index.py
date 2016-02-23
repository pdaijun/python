#coding:utf-8
from main import login
from main import classs
import sys
import time
import json
from main.login import write_zd
login.init_zd()
zhangdan=[]
print '欢迎来到网上银行'
login.init_database()
flags=False
while flags is False:
    username=raw_input('Username:')
    password=raw_input('Password:')
    flags=login.login(username,password)
    if flags is False:
        print '请重新输入'
account=classs.account_info(username)
print '''
姓名      %s
余额     %s
''' %(username,account.balance())
func=['get_money','save_money','check_zhangdan','exit']
for i in enumerate(func,1):
    print str(i).strip('()')
while True:
    foo=input('请选择:')
    if foo == 1 or foo == 'get_money':
        money=input('请输入金额')
        account.get_money(money)
        zhangdan.append("%s   %s   %s" %(time.time(),'get_money',money))
        print '余额 : %s' % account.balance()
    elif foo == 2 or foo== 'save_money':
        money=input('请输入金额')
        account.save_money(money)
        print '余额 : %s' % account.balance()
        zhangdan.append("%s   %s   %s" %(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),'save_money',money))
    elif foo ==3 or foo == 'check_zhangdan':
        for i in zhangdan:
            print i
    elif foo == 4 or foo == 'exit':
        write_zd(zhangdan)
        break


    
    