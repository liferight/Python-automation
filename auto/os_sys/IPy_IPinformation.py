#!/usr/bin/env python
# coding:utf-8
from IPy import IP
ip_s = raw_input('please input an ip or net-range:')

ips = IP(ip_s)
if len(ips) > 1:
	print('net: %s' % ips.net())
	print('netmask: %s' % ips.netmask())
	print('broadcast: %s' % ips.broadcast())
	print('reverse address: $s' % ips.reverse())
	print('subnet: %s' % len(ips))
else:
	print('方向地址: %s' % ips.reverseNames()[0])
	print('hexadecimal: %s' % ips.strHex())
	print('binary ip: %s' % ips.strBin())
	print('iptype: %s' % ips.iptype())
	
