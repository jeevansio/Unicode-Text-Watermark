# -*- coding: utf-8 -*-

#this hash input: bytes
#Another way to tranformation str and bytes:
#bytes=str.decode('UTF-8')；str=bytes.encode('UTF-8')


passwd = b'2017301510035'  #bytes type
text=b'ILOVEU'*100

import hmac

hm = hmac.new(passwd,text)
wm = hm.hexdigest()
print('len=%d,hexwm=%s'%(len(wm),wm))
wm2=bin(int(wm, 16))
#the transformation above leaves "0b" so we have to del the first 2
wm2=wm2[2:]
print('len=%d,binwm=%s'%(len(wm2),str(wm2)))

#test shows that output type=str,len=128bit(after del)



















