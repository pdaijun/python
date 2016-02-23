#coding:utf-8
'''
import MySQLdb
conn = MySQLdb.connect(host='10.203.0.28',user='root',passwd='redhat',db='python')
cur = conn.cursor()
reCount = cur.execute('select * from UserInfo')
data = cur.fetchall()
cur.close()
conn.close()
print reCount
print data

import MySQLdb
conn = MySQLdb.connect(host='10.203.0.28',user='root',passwd='redhat',db='python')
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) # 以字典的方式接受

#sql = "insert into UserInfo (name,age) values(%s,%s)"
#params =  ('zles',18,)
#sql = "delete from UserInfo where id = %s"
#params = (2,)
#sql = "update UserInfo set name = %s where id = %s"
#params = ('sb',8)
#reCount = cur.execute(sql ,params)
params=[
        ('sx',19),
        ('sb',20),
        ('ax',20),
        ]
reCount = cur.executemany('insert into UserInfo(name,age) values(%s,%s)',params)

conn.commit()
cur.close()
conn.close()

print  reCount

import MySQLdb
conn = MySQLdb.connect(host='10.203.0.28',user='root',passwd='redhat',db='python')
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) 
reCount = cur.execute("select * from UserInfo")
data =cur.fetchall()
conn.commit()
cur.close()
conn.close()
print reCount
print data

'''

import MySQLdb
conn = MySQLdb.connect(host='10.203.0.28',user='root',passwd='redhat',db='python')
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) 
reCount = cur.execute("select * from UserInfo")
data =cur.fetchone()
print data
data =cur.fetchone()
print data
data =cur.fetchone()
print data
data =cur.fetchone()
print data
data =cur.fetchone()
print data
data =cur.fetchone()
print data
data =cur.fetchone()
print data
data =cur.fetchone()
print data
data =cur.fetchone()
print data
conn.commit()
cur.close()
conn.close()
print reCount

