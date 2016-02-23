#coding:utf-8
import sys,json

def init_database():
    with open('account.json','wb') as data:
        account_info={'daijun':'daijun123','peng':'daijun123'}
        json.dump(account_info,data)
    

def login(username,password):    
    account=json.load(open('account.json','rb'))
    if username in account and password == account[username]:
        match_flags = True 
        return match_flags
    else:
        match_flags = False
        return match_flags
      #  if match_flags is True:
       #     return match_flags
            
        #else:
        #        print '帐号密码不匹配，请重新输入'
        
def init_zd():
    with open('zhangdan.json','wb') as init_zd:
        json.dump(['时间    动作   金额'],init_zd)       
def write_zd(zhangdan):
    with open('zhangdan.json','ab') as w_zhangdan:
        json.dump(zhangdan,w_zhangdan)
'''
account=json.load(open('account.json','rb'))
for key,value in account.items():
    print key,value
   '''