# -*- coding: utf-8 -*-

#this hash input: bytes
#Another way to tranformation str and bytes:
#bytes=str.decode('UTF-8')；str=bytes.encode('UTF-8')


passwd = b'2017301511111'  #bytes type
text=b'ILOVEU'*100

import hmac

'''
this is wrong since I didn't realize that the function will lose some bits

hm = hmac.new(passwd,text)
wm = hm.hexdigest()
print('len=%d,hexwm=%s'%(len(wm),wm))
#next we need to tranform wm from hex to dec to bin
wm2=bin(int(wm, 16))
#the transformation above leaves "0b" so we have to del the first 2
wm2=wm2[2:]
print('len=%d,binwm=%s'%(len(wm2),str(wm2)))'''

#test shows that output type=str,len=128bit(after del)

'''This is a good one!!'''
def myhash(value,key):
	hm = hmac.new(key,value)
	wm = hm.hexdigest( ) 
	#len=32,str,hex,eg"5157f56c40e7d4964bf9bca8e4fb9a63"
	str=''
	for i in range(len(wm)):
		temp=bin(int((wm[i]),16))
		temp=temp[2:]
		lent=len(temp)
		temp='0'*(4-lent)+temp
		str=str+temp
	print(str)
	print(len(str))
	return str

#finally output is str,type=str,len=128

watermark=myhash(text,passwd)

















