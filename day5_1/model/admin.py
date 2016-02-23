#coding:utf-8

from mysql.helpmysql import Mysqlhelper
class Admin(object):
    
    def __init__(self):
        self.__helpsql=Mysqlhelper()
    def Get_Name_passwd(self,user,passwd):
        sql="select * from account where name = %s and passwd = %s"
        parms=(user,passwd,)       
        return self.__helpsql.Get_fetchone(sql, parms)
    
        