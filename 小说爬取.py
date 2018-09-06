'''
Created on 2018年9月1日

@author: Admin
'''
from web import Url
from web import Zhengzhe

from web import Save

if __name__ == '__main__':
    #url="https://acg12.com/278708/"
    url="https://www.qiushibaike.com/"
    gethtml=Url.Url(1)
    html=gethtml.getHtml_headers(url)
   
    print(html)
    
    #z=Zhengzhe.Zhengzhe()
    #imgList=z.getAllImg(html)
    
    #s=Save.Save()
    #s.downLodSave(imgList, 'img')
    
    
    #print(imgList)
    pass