# -*- coding:utf-8 -*-
'''
Created on 2018年9月1日

@author: Admin
'''
from web import Url
from web import Zhengzhe
import time
from web import Save


if __name__ == '__main__':
    #url="https://acg12.com/278708/"
    #https://www.qiushibaike.com/8hr/page/1/
    z=Zhengzhe.Zhengzhe()
    f=open('html.txt','w',encoding="utf-8");
    for page in range(1,20):
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
    