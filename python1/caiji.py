#!F:\python\python.exe
# -*- coding: UTF-8 -*-
#把配置文件读取过来
from db import *
from bdnews import *
news = News()

# arr=news.getNav()
# str1=''
# for item in arr:
# 	site_name= item[0].lstrip('"')
# 	site_url=news.tranTags(item[1])
# 	str='("'+site_name+'","'+site_url+'"),'
# 	str1+=str
# nav=str1[:-1]
# sql="insert into news (site_name,site_url) values"+ nav
# db=DB()
# res=db.my_add(sql)
arr=news.getBiao()
str1=''
for item in arr:
    site_name= item[0].lstrip('"')
    site_url=item[1]
    str="("+"'"+site_name+"'"+","+"'"+site_url+"'"+")"+","
    str1+=str
nav=str1[:-1]
sql="insert into news (site_name,site_url) values"+ nav
db=DB()
res=db.my_add(sql)
print res
	

