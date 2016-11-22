#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
import smtplib
import string

HOST = "smtp.xxx"
SUBJECT = "test email form zyn"
TO = "xxx@qq.com"
FROM = "xxxx@xx.com"
text = "test"
BODY = string.join(( 
		"From: %s" % FROM,
		"To: %s" % TO,
		"Subject: %s" % SUBJECT,
		"",
		text), "\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("xxx@xx.com","123456")
server.sendmail(FROM, [TO], BODY)
server.quit()
