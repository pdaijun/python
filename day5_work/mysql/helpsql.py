#coding:utf-8
import MySQLdb
import conf
class Mysql_account(object):
    
    def __init__(self):
        self.__conn=conf.talk  
    
    def Get_account_fetchall(self,sql,parprams=None):
        conn=MySQLdb.connect(**self.__conn)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)       
        reCont = cur.execute(sql,parprams)
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return data
    
    def Get_account_fetchone(self,sql,parprams):
        conn=MySQLdb.connect(**self.__conn)
        cur=conn.cursor()
        reCont = cur.execute(sql,parprams)
        data = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return data
'''
class Mysql_message(object):
    
    def __init__(self):
        self.__conn=conf.message
    
    def Get_message_fetchall(self,sql,parprams):
        conn=MySQLdb.connect(**self.__conn)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)       
        reCont = cur.execute(sql,parprams)
        data = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return data
    
    def Get_message_fetchone(self,sql,parprams):
        conn=MySQLdb.connect(**self.__conn)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        reCont = cur.execute(sql,parprams)
        data = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return data
'''
    