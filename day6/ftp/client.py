#coding:utf-8
import socket
import os
ip_port = ('10.203.0.28',7777)
sk = socket.socket()
sk.connect(ip_port)
while True:
    input =raw_input('path:')
    #cmd: put get 
    # path 路径
    cmd,path = input.split('|')
    file_name = os.path.basename(path)
    file_size=os.stat(path).st_size
    
    sk.send(cmd+"|"+file_name+'|'+str(file_size))
    send_size = 0
    f = file(path,'rb')
    Flag = True
    while Flag:
        if send_size + 1024 > file_size:
            data = f.read(file_size-send_size)
            Flag = False
        else:
            data = f.read(1024)
            send_size +=1024
        sk.send(data)
        f.close()
sk.close()
            