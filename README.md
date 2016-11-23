# Python-automation

刚开始学习python自动化运维，希望大家一起成长

1.系统性能信息模块psutil

2.IP地址处理模块IPy

3.DNS处理模块dnspython

4.文件内容差异对比difflib

5.文件与目录差异对比filecmp

6.发送电子邮件模块smtplib

7.探测web服务质量pycurl

#auto各个脚本信息
IPy_IPinformation.py  获取ip详细信息
dnspython.py 域名解析
dnspython_ns.py  域名A记录
dnspython_mx.py  域名MX记录
dnspython_cname.py 域名CNAME
dns_monitor.py  监控域名80端口，适用于dns轮训
diffmonitor.py  对比字符串直接打印
diffmonitor_html.py  对比字符串输出到HTML格式
diff_nginx.py 对比nginx配置文件 python diff_nginx.py nginx_1.conf nginx_2.conf >> test.html
diff_filecmp.py  校验源与备份目录的差异，使用filecmp模块的left_only、diff_files方法递归获取源目录的更新选项，再通过shutil.copyfile、os.makedirs方法对更新项进行复制，最终保持一致。
