#!/usr/bin/env python
import difflib
text1 = """text1:	#定义字符串1
this module
difflib document v7.4
add string
"""
text1_lines = tex1.splitlines()		#以行进行分割 以便进行对比
text2 = """text2:	#定义字符串2
this module
difflib document v7.5"""
text2_lines = text2.splitlines()
d = difflib.Differ()   #创建Differ()对象
diff = d.compare(text1_lines, text2_lines)  #采用commipare方法对比字符串
print '\n'.join(list(diff))

