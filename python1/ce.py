#!F:\python\python.exe
# -*- coding: UTF-8 -*-
#把配置文件读取过来
print "Content-type:text/html;charset=UTF-8"
print
# CGI处理模块
import cgi, cgitb 
import re
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 
from db import *
uname = form.getvalue('uname')
pwd  = form.getvalue('pwd')
rpwd = form.getvalue('rpwd')
phone  = form.getvalue('phone')
smail = form.getvalue('smail')
jie  = form.getvalue('jie')
#用户验证
a=re.compile("^[0-9a-z]{5,9}$")
q=a.match(uname)
if (q):
	print ok
else:
	print "<script>alert('用户需要5-10为数字或者字母');location.href='a.html'</script>"
#密码
a=re.compile("^[0-9]{5,9}")
pwd=a.match(pwd)
if (pwd):
	print ok
else:
	print "<script>alert('密码需要5-10为数字');location.href='a.html'</script>"
#密码
a=re.compile("^[0-9]{5,9}")
rpwd=a.match(rpwd)
if (rpwd==pwd):
	print ok
else:
	print "<script>alert('密码需要5-10为数字');location.href='a.html'</script>"
#手机号
a=re.compile("^1[3,5,9]\d{9}$")
q=a.match(phone)
if (q):
	print ok
else:
	print "<script>alert('手机号必须是13,15,19为数字的11位数');location.href='a.html'</script>"
#邮箱
a=re.compile("^\w+@\w+(\.)(com|cn)$")
q=a.match(smail)
if (q):
	print ok
else:
	print "<script>alert('邮箱格式为22@qq.com');location.href='a.html'</script>"
#简介
a=re.compile("^[\u2E80-\u9FFF]+$")
q=a.match(jie)
if (q):
	print ok
else:
	print "<script>alert('简介必须是汉字');location.href='a.html'</script>"




# sql = "INSERT INTO python (uname,pwd,rpwd,phone,smail,jie) values (1111,2222)"
# db=DB()
# print(db.my_add(sql))
