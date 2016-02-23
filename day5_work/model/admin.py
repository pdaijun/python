#coding:utf-8
from mysql import helpsql
import SocketServer
class account(object):
    def __init__(self):
        self.__sql=helpsql.Mysql_account()
        
    def select_one(self,user,passwd):
        sql='select id from account where username=%s and password=%s'
        parms=(user,passwd,)
        return self.__sql.Get_account_fetchone(sql, parms)
class message(object):
    def __init__(self):
        self.__sql=helpsql.Mysql_account()
    
    def select_all(self):
        sql = 'select * from message'
        return  self.__sql.Get_account_fetchall(sql)
    
    def Inset_one(self,MESSAGE,TIME,UID):
        sql = 'insert into messages(MESSAGE,TIME,UID) values(%s,%s,%s)'
        parms=(MESSAGE,TIME,UID,)
        return self.__sql.Get_account_fetchone(sql, parms)

        
    