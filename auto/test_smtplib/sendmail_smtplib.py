#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
import smtplib
import string

HOST = "smtp.daojia.com.cn"
SUBJECT = "test email form zyn"
TO = "673749764@qq.com"
FROM = "zhangyanan@daojia.com.cn"
text = "test"
BODY = string.join(( 
		"FROM: %s" % FROM,
		"TO: %s" % TO,
		"Subject: %s" SUBJECT,
		"",
		test), "\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("zhangyanan@daojia.com.cn","yanan1989")
server.sendmail(FROM, [TO], BODY)
server.quit()