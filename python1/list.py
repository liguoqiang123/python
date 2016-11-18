#!F:\python\python.exe
# -*- coding: UTF-8 -*-

print "Content-type:text/html"
print                               # 空行，告诉服务器结束头部
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("127.0.0.1","root","root","yii" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM python "
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      username = row[1]
      url = row[2]
      # 打印结果
      print "id=%s,username=%s,url=%s" % \
             (id, username, url)
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()