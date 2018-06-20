#!/usr/bin/env python
#from zyn
#coding:utf8
import re
import os
import time
import smtplib
import socket
import fcntl
import struct
from email.mime.text import MIMEText
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
   
def sendemail(subject,msg,fromemail,emailpasswd,toemail):
    '''实现发送邮件功能函数'''
    _user = fromemail
    _pwd  = emailpasswd
    _to   = toemail
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
     
    msg = MIMEText(msg,format,'utf-8')
    if not isinstance(subject,unicode):
        subject = unicode(subject)
    msg["Subject"] = subject
    msg["From"]    = _user
    msg["To"]      = ",".join(_to) 
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,utf-8"
         
    try:
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print "[%s]INFO:Email send Success!" % nowtime
    except smtplib.SMTPException,e:
        print "[%s]ERROR:Email send Falied,%s" % (nowtime,e) 
def matchkeyword(pattern,alertlogfile):
    '''实现匹配关键字函数'''
    re.compile(pattern)
    posfile = "/tmp/posfile"
    if not os.path.exists(posfile):
        os.mknod(posfile)
    if not os.path.getsize(posfile):
        with open(posfile,'w') as fobj:
            fobj.write('0')       
    #打开文件
    f = open(alertlogfile,'r')
    #移动到文件结尾
    f.seek(0,2)
    #读出文件所在的字节位置
    endpos = f.tell() 
    #移动到文件的开头
    with open(posfile,'r') as fobj:
        startpos = int(fobj.read())
        f.seek(startpos)
         
    if endpos-startpos > 0:    
        data = f.read(endpos-startpos)
        f.close()
        with open(posfile,'w') as fobj:
            fobj.write(str(endpos))
        m = re.findall(pattern, data,re.IGNORECASE)
        if m:
            content = '\n'.join(m)    
            return content
        else:
            return ''
             
if __name__ == '__main__':
    local_ip = get_ip_address('eth0')
    subject = '服务器[%s]日志报警了！' % local_ip
    fromemail = 'xxxxxxxx@qq.com'
    #emailpasswd为QQ邮箱的授权码
    emailpasswd = 'mdkuasfhnjbrbhdj'
    toemail = ['xxxxxx@qq.com','yyy@qq.com']
    alertlogfile = "/data/mysql/mysql_3306/log/error.log"
    #pattern = ".*\[Warning\].*\s|.*\[Note\].*\s"
    pattern = ".*Warning.*\s|.*error.*\s"
    while True:
        content = matchkeyword(pattern, alertlogfile)
        if content:
            sendemail(subject, content, fromemail, emailpasswd, toemail)