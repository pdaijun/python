#coding:utf-8
from model import admin


def main():
    user=raw_input("Username")
    passwd=raw_input("password")
    login=admin.Admin()
    results = login.Get_Name_passwd(user,passwd)
    if not results:
        print 'connet is falid'
    else:
        print results
if __name__ =='__main__':main()