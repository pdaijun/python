#coding:utf-8

import socket
ck=socket.socket()   #建立sock
ip_port=("localhost",7777)   
ck.connect(ip_port) # 连接服务器
while True:
    data=ck.recv(1024)   #接受数据
    print data
    Send=raw_input('clent:')
    ck.send(Send)
    if Send =='exit':
        break
ck.close()

