import urllib
import urllib2
import re
from db import *
class News:

    #init
    def __init__(self):
        self.url = "http://news.baidu.com/"

    # jie  qu  div
    def tranTags(self, x):
        pattern = re.compile('<div.*?</div>')
        res = re.sub(pattern, '', x)
        return res

    #get qing qiu
    def getPage(self):
        url = self.url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

   #cai ji daohang
    def getNavCode(self):
        page = self.getPage()
        pattern = re.compile('(<div id="menu".*?)<i class="slogan"></i>', re.S)
        navCode = re.search(pattern, page)
        return navCode.group(1)
        
    #cai ji bianqian
    def getNav(self):
        navCode = self.getNavCode()
        pattern = re.compile('<a href=("http://.*?/).*?>(.*?)</a>', re.S)
        itmes = re.findall(pattern, navCode)
        return itmes
    # caiji  biaoti
    def getHang(self):
        page = self.getPage()
        pattern=re.compile('<div id="pane-news".*?>(.*?)<div .*? alog-group=log-mil-middle>',re.S)
        navCode = re.search(pattern, page)
        return navCode.group()
    def getBiao(self):
        navCode = self.getHang()
        pattern = re.compile('<span class="dot"></span>.*?<a href=("http://.*?/).*?>(.*?)</a>', re.S)
        itmes = re.findall(pattern, navCode)
        return itmes










