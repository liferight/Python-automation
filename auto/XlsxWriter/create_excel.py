#!/usr/bin/env python
# coding:utf-8
#create zyn 2016

import xlsxwriter

workbook = xlsxwriter.Workbook('t9.xlsx') #创建一个excel文件
worksheet = workbook.add_worksheet()  #创建一个工作表对象

worksheet.set_column('A:A', 20)  #设定第一列宽度为20像素
bold = workbook.add_format({'bold': True}) #定义一个加粗额格式对象

worksheet.write('A1', 'hello')  #A1单元格写入hello
worksheet.write('A2', 'World', bold) #A2单元格写入world，并引用加粗格式对象bold
worksheet.write('B2', u'中文测试', bold) #B2单元格写入中文并引用加粗格式对象bold

worksheet.write(2, 0, 32) #用行列表示法写入数字‘32’与‘35.5’
worksheet.write(3, 0, 35.5) #行列表示法的单元格下标以0作为起始值，‘3,0’等价于A3
worksheet.write(4, 0, '=SUM(A3:14)') #求A3A4的和，并将结果写入‘4,0’ 即A5

worksheet.insert_image('B5', 'img/t9.jpg') #在B5单元格插入图片
workbook.close()

