#!F:\python\python.exe
# -*- coding: UTF-8 -*-
print "Content-type:text/html"
print
# CGI处理模块
import cgi, cgitb 
import MySQLdb
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_name = form.getvalue('username')
site_url  = form.getvalue('url')
db = MySQLdb.connect("127.0.0.1","root","root","yii" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO python (username,url) values ("+"'"+site_name+"'"+","+"'"+site_url+"'"+")"

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
   print "<script>alert('登陆成功');location.href='list.py'</script>"
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()
