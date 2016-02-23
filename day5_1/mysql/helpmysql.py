#coding:utf-8
import MySQLdb
import config
class Mysqlhelper(object):
    
    def __init__(self):
        self.__conn=config.conn  
    
    def Get_fetchall(self,sql,parprams):
        conn=MySQLdb.connect(**self.__conn)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)       
        reCont = cur.execute(sql,parprams)
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return data
    
    def Get_fetchone(self,sql,parprams):
        conn=MySQLdb.connect(**self.__conn)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        reCont = cur.execute(sql,parprams)
        data = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return data
'''
helper=Mysqlhelper()
sql="select * from UserInfo where id > %s"
parprams = (4,)
result=helper.Get_fetchall(sql,parprams)
print result
sql="select * from UserInfo where id > %s"
parprams = (4,)
result=helper.Get_fetchone(sql,parprams)
print result
'''