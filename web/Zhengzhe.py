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
            