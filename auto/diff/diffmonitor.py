#!/usr/bin/env python

import difflib

text1 = """text1:
this module
difflib document v7.4
add string
"""
text1_lines = text1.splitlines()
text2 = """text2:
this module
difflib document v7.5"""
text2_lines = text2.splitlines()
d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print '\n'.join(list(diff))

