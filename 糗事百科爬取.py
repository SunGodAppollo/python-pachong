# -*- coding:utf-8 -*-
'''
Created on 2018年9月1日

@author: Admin
'''
from web import Url
from web import Zhengzhe
import time
import sys
from web import Save


if __name__ == '__main__':
    #url="https://acg12.com/278708/"
    #https://www.qiushibaike.com/8hr/page/1/
    z=Zhengzhe.Zhengzhe()
    fileTime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    #print(fileTime)
    #sys.exit(0)

    f=open(fileTime+'糗事百科.txt','w',encoding='utf_8_sig')
    for page in range(1,10):
        url="https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
        gethtml=Url.Url(1)
        html=gethtml.getHtml_headers(url)

        #print(html)


        imgList=z.getAllqiushi(html)


        for i in imgList:
            mystr=i.strip()
            mystr=mystr.replace('<br/>','\n')
            print(mystr)
            saveStr=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"\n"+mystr+"\n"
            f.writelines(saveStr)
    f.close()
    print("end")
    #print(html)
