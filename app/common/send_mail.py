# -*- coding: utf-8 -*-
import os,smtplib,os.path
from email.mime.image import MIMEImage
import app.config.globalparameter as gl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from bs4 import BeautifulSoup
from app.log.log import atp_log
#定义邮件内容
def send_email():
    try:
        #写html
        write_html()
        #邮件的配置项：发件人，收件人，标题，用户及密码
        sender='cherrylixh@pptv.com'
        reciever=['cherrylixh@pptv.com']
        subject='Tvsports Daily Stability Auto Test 3.7.1 on '+gl.ipport()
        smtpserver='mail.pptv.com'
        username = 'cherrylixh'
        password = 'Liluo12345678@'
        # username=gl.email_name
        # password=gl.email_password
        #获取测试报告的路径
        new_report=gl.newreport()
        #创建一个带附件的邮件实例
        msg = MIMEMultipart()

        f=open(new_report+'test.html','rb')
        mail_body=f.read()
        f.close()
        part=MIMEText(mail_body,'html','utf-8')
        msg.attach(part)

        #打开图片目录
        pnglist=[gl.cputotall,gl.cpuppdata,gl.memtotall,gl.memppdata]
        for png in pnglist:
            fp_png=open(new_report+png+'.png','rb')
            msgImage=MIMEImage(fp_png.read())
            fp_png.close()
            msgImage.add_header('Content-ID', '<%s>' % png)
            msg.attach(msgImage)
        # 以测试报告作为文件内容
        # f1=open(new_report+'result.html','rb')
        # mail_body1=f1.read()
        # f1.close()
        # 将BeautifulReport
        # part1=MIMEText(mail_body1,'html','utf-8')
        # msg.attach(part1)

        msg['Subject']=Header(subject,'utf-8')
        smtp=smtplib.SMTP()
        server = SMTP_SSL(host=gl.smtp_server)
        smtp.connect(smtpserver,587)
        smtp.set_debuglevel(1)
        smtp.login(username,password)
        smtp.sendmail(sender,reciever,msg.as_string().encode('ascii'))
        smtp.quit()
    except Exception as e:
        print('邮件发送失败')
        atp_log.error('邮件发送失败')
#手动写html，将png图片加载到html中
def write_html():
    try:
        #获取图片路径
        new_report=gl.newreport()
        mhtml=new_report+'test.html'
        f=open(mhtml,'w')
        f.close()
        Fobj=open(mhtml,encoding='utf-8')
        data=Fobj.read()
        Fobj.close()
        # soup=BeautifulSoup(data,'lxml')
        write_report=open(mhtml,'a+')
        # 将png写到html用，用cid content-id方式
        write_report.write("</br><strong>" + "TVsports Ram chart:" + "</strong></br>")
        write_report.write("<img src='cid:%s'/></br>" %gl.memtotall)
        write_report.write("<img src='cid:%s'/></br>" %gl.cputotall)
        write_report.write("<img src='cid:%s'/></br>"%gl.cpuppdata)
        write_report.write("<img src='cid:%s'/></br>"%gl.memppdata)
        write_report.write("<img src='cid:%s'/></br>"%gl.cpuguard)
        write_report.write("<img src='cid:%s'/></br>"%gl.memguard)
        # write_report.write("<img src='cid:ppdata'/>" + "</br>")
        write_report.close()
    except Exception as e:
        print('写入html失败')
        atp_log.error('写入html失败')
if __name__=='__main__':
    send_email()
