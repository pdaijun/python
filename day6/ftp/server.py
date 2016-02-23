#coding:utf-8
import os  
import SocketServer
#多线程加异步
class MyServer(SocketServer.BaseRequestHandler):    
    def setup(self):
        pass
    def handle(self):
        base_path='C:/temp'
        conn = self.request
        print "connected..."
        while True:
            pre_data = conn.recv(1024)
            cmd,file_name,file_size = pre_data.split('|')
            recv_size = 0
            file_dir = os.path.join(base_path,file_name)
            f = file(file_dir,'wb')
            Flag = True
            while Flag:
                if int(file_size) > recv_size:
                    data = conn.recv(1024)
                    recv_size += len(data)
                    f.write(data)
                else:
                    recv_size = 0
                    Flag = False                
            print 'upload successed'
            f.close()
    def finish(self):
        pass
if __name__=='__main__':
    server=SocketServer.ThreadingTCPServer(('127.0.0.1',7777),MyServer)
    server.serve_forever()
    server.handle()