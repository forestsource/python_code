#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii

#name = raw_input("拡張子:")
str = raw_input("バイナリ:")
str = str.split("\\")
if (str[0] == ''):
	str.pop(0)
List16 = list()
List10 = list()
for octet in str:
  t = int(octet,8)
  List10.append(t)
  t = hex(t)
  List16.append(t)
binary = ' '.join(List16)
print binary
#print "16進数: "+str(binary)
asciis = ' '.join([chr(x) if(127>x>22)else "." for x in List10])
print asciis
#print "ASCii: " + map(str,asciis)
#print name + "|" + str(binary) + "|" + asciis