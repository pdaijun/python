#coding:utf-8
#客户端与服务端交互
'''
import socket

sk=socket.socket()   # 建立sock
ip_port=("localhost",9090)
sk.bind(ip_port) 
sk.listen(5)
while True:
    connetion,ipaddr=sk.accept()  #connetion 客户端的sock ipaddr客户端的地址和端口      #链接数
    connetion.send('hello')   #向客户端发送数据
    flags = True
    while flags is True: 
        data=connetion.recv(1024)
        print data
        if data =='exit':
            flags = False
        else:
            Send=raw_input('server:')
            connetion.send(Send)
    connetion.close()     #断开连接
'''    
import SocketServer
#多线程加异步
class MyServer(SocketServer.BaseRequestHandler):    
    def setup(self):
        pass
    def handle(self):
       # print self.client_address
        conn=self.request
       # print self.server
        conn.send('hello')
        flags = True
        while flags is True: 
            data=conn.recv(1024)
            print data
            if data =='exit':
                flags = False
            else:
                Send=raw_input('server:')
                conn.send(Send)
        conn.close() 
    def finish(self):
        pass
if __name__=='__main__':
    server=SocketServer.ThreadingTCPServer(('127.0.0.1',7777),MyServer)
    server.serve_forever()
    server.handle()