#!/usr/bin/env python2.7
'''
An example of reading and writinng Unicode strings:Write
a Unicode string to a file in utf-8 and reads it back in.
'''
CODEC='utf-8'
FILE='unicode.txt'

hello_out=u"hello world\n"
bytes_out=hello_out.encode(CODEC)
f=open(FILE,'w')
f.write(bytes_out)
f.close()

f=open(FILE,'r')
bytes_in=f.read()
f.close()
hello_in=bytes_in.decode(CODEC)

print hello_out