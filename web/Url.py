'''
Created on 2018年9月1日

@author: Admin
'''
import urllib.request


class Url(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
    def getHtml(self,url):
        response = urllib.request.urlopen(url, timeout=10)
        return response.read().decode("utf-8")
    def getHtml_headers(self,url):
        request = urllib.request.Request(url, data=None, headers=self.headers)
        return urllib.request.urlopen(request, timeout=10).read().decode("utf-8")
        