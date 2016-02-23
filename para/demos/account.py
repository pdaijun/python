#coding:utf-8
import os
import MySQLdb
import SocketServer
class Mysql_account(object):
    
    def __init__(self):
        self.__conn=dict(host='10.203.0.28',user='root',passwd='redhat',db='python')      
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
class account(object):
    def __init__(self):
        self.__sql=Mysql_account()
    def select_all(self,user):
        sql='select HOSTNAME,USERNAME,PASSWORD from HOST_USER_PASSWD where username=%s '
        parms=(user,)
        return self.__sql.Get_account_fetchall(sql, parms)
    def select_one(self,hostname,user):
        sql='select PASSWORD from HOST_USER_PASSWD where username=%s and hostname=%s '
        parms=(user,hostname)
        return self.__sql.Get_account_fetchone(sql, parms)
if __name__=='__main__':
    X=account()
    #X_RES=X.select_all(os.getlogin())
    X_RES=X.select_all('daijun')
    host_list=[]
    for i in X_RES:
        host_list.append(i['HOSTNAME'])
    for i in range(len(host_list)):
        print i+1 ,host_list[i]
    Flags=False
    while Flags is False:
        HOST=input("请选着主机序号eg:1or2")
        try :
            HOSTNAME=host_list[HOST]
            Flags = True
        except e :
            print e
    #USER=(os.getlogin())
    PASS=X.select_one(HOSTNAME, 'daijun')
    PASSWD=PASS[0]
    print PASSWD
    password='redhat'
    print password
    