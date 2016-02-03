import binascii
str = raw_input()
str = str.split("\\")
if (str[0] == ''):
	str.pop(0)
strList = list()
for octet in str:
  t = int(octet,8)
  t = hex(t)
  strList.append(t)
print ' '.join(strList)
