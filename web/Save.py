'''
Created on 2018年9月1日

@author: Admin
'''
import urllib.request
class Save(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
    def downLodSave(self,list,path):
        
        thisTime=''
        x=0
        for imgurl in list:
            x+=1
            savePath=path+str(x)+'.jpg'
            print(savePath)
            print(imgurl)
            f=open(savePath,'wb')
            request = urllib.request.Request(imgurl, data=None, headers=self.headers)
            f.write(urllib.request.urlopen(request, timeout=10).read())
            f.close()
           
