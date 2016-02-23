#coding:utf-8
from model import admin
import SocketServer
import time
'''
模仿聊天，客户端发信息给服务端，过滤一些敏感信息然后给客户端恢复信息并把聊天信息记录到数据库
'''
class MyServer(SocketServer.BaseRequestHandler):
    '''
    def __init__(self,UID):
        SocketServer.BaseRequestHandler.__init__(self)
        self.__uid=UID  
    '''    
    def handle(self):
        conn=self.request
        while True:
            conn.send('username:')
            user=conn.recv(1024)
            conn.send('password:')
            passwd=conn.recv(1024)        
            login=admin.account()
            UID = login.select_one(user,passwd)
            if not UID:
                conn.send('connet is falid')
                conn.recv(1024)
            else:
                conn.send("登录成功 想说些什么")
                break
        flags = True
        while flags is True: 
            data=conn.recv(1024)
            TIME=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            C=admin.message()
            C.Inset_one(data,TIME,UID)        
            if data.count('sb'):
                conn.send('ni cai shi  sb')
            elif data.count('sx'):
                conn.send('ni caishi sx')
            elif data.count('daijun'):
                conn.send('shi daijun')
            elif data == 'exit':
                flags = False
            else: 
                conn.send(' wo bu zhidao  zm ban ')
        conn.close()

server=SocketServer.ThreadingTCPServer(('127.0.0.1',8888),MyServer)
server.serve_forever()
server.handle()





















'''
mysql=admin.message()
mysql.Inset_one('daijun', '2010-10-10 20:20:22', 1)



from mysql import helpsql
x=helpsql.Mysql_account()
sql="insert into messages(MESSAGE,TIME,UID) values(%s ,%s, %s)"
parm=('daijun','1020-2002-202 10:202:20','1')
y=x.Get_account_fetchall(sql,parm)
'''
