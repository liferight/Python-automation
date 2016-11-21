#!/usr/bin/env python
# coding:utf-8
import dns.resolver

domain = raw_input('please input an domain:') #输入域名地址
		
MX = dns.resolver.query(domain, 'MX')
for i in MX.response.answer:
	print 'MX preference=', i.preference, 'mail exchanger', i.exchange
