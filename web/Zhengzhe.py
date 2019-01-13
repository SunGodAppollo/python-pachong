'''
Created on 2018年9月1日

@author: Admin
'''
import re

class Zhengzhe(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def getAllImg(self,html):
        pattern = re.compile(r'<img src="(.*?)" .*?>')   # 查找数字
        return pattern.findall(html)
    def getAllpipe(self,html,reString):
        pattern = re.compile(reString)   # 查找数字
        return pattern.findall(html)
    def getAllqiushi(self,html):
        pattern = re.compile(r'<div class="content">.*?<span>(.*?)</span>.*?</div>',re.S)   # 查找数字
        return pattern.findall(html)
    def getqingxiaoshuocontent(self,html):
        pattern = re.compile(r'<div class="article-content font16" .*?>(.*?)</div>',re.S)   # 查找内容
        return pattern.findall(html)
    #<h1 class="article-title">第一章 日常（1）</h1>
    def gettitle(self,html):
        pattern = re.compile(r'<h1 class="article-title">(.*?)</h1>',re.S)   # 查找内容
        return pattern.findall(html)
    # <a href="/Novel/171482/271580/2324375/" class="btn normal">下一章</a>
    def getnexturl(self,html):
        pattern = re.compile(r'上一章</a>.*?<a href="(.*?)" class="btn normal">下一章</a>',re.S)   # 查找内容
        return pattern.findall(html)
