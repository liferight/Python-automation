#!/usr/bin/env python
# coding:utf-8
import dns.resolver

domain = raw_input('please input an domain:') #输入域名地址
ns = dns.resolver.query(domain, 'NS')  #指定查询类型为A记录
for i in ns.response.answer:			 #通过response.answer方法获取查询回应信息
	for j in i.items:				 #遍历回应信息
		print j.to_text()
