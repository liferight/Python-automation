#!/usr/bin/env python
# coding:utf-8
import dns.resolver

domain = raw_input('please input an domain:') #输入域名地址
cname = dns.resolver.query(domain, 'CNAME')  #指定查询类型为A记录
for i in cname.response.answer:			 #通过response.answer方法获取查询回应信息
	for j in i.items:				 #遍历回应信息
		print j.to_text()
