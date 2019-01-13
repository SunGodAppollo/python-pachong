# -*- coding:utf-8 -*-
'''
Created on 2018年9月1日

@author: Admin
'''
from web import Url
from web import Zhengzhe
import time
import sys
import os
from web import Save

z=Zhengzhe.Zhengzhe()

#网站域名
host="http://book.sfacg.com/"
#第一章地址
start_page_url="http://book.sfacg.com/Novel/139025/226111/1886106/"
#书名
bookname="可怕的后宫们与日渐消瘦的我关于我家女仆是大小姐这件事"
#自增长序号
pageIndex=1

def getPage(pageurl):
    global pageIndex
    gethtml=Url.Url(1)
    url=pageurl
    html=gethtml.getHtml_headers(url)
    #获得标题
    title=z.gettitle(html) #标题
    title="".join(title)
    title='第'+str(pageIndex)+'章 '+title
    #存储内容
    file_path='./'+bookname+'/'+title+'.txt'
    #判断路径是否存在
    if not os.path.exists(bookname):
        os.makedirs(bookname)
    #打开文件
    f=open(file_path,'w',encoding='utf_8_sig')
    #写文件
    contentList=z.getqingxiaoshuocontent(html)
    f.writelines(title+'\n')#填写标题
    for i in contentList:
        mystr=i.strip()
        mystr=mystr.replace('</p>','\n')
        mystr=mystr.replace('<p>','')
        mystr=mystr.replace('<br>','')
        #print(mystr)
        saveStr=mystr
        f.writelines(saveStr)
    f.close()
    #输出显示
    print(title)
    pageIndex=pageIndex+1
    #获得下一章节连接
    nexurl=z.getnexturl(html) #下一章连接
    nexurl="".join(nexurl)
    nexurl=host+nexurl
    #print(nexurl)
    return nexurl







if __name__ == '__main__':
    nex_url=start_page_url
    while True:
        nex_url=getPage(nex_url)
        if nex_url==host:
            break
