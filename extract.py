#author:ly
#function:extract wm

from functools import reduce

original_code = [   u"\u002d", u"\u003b", u"\u0043", u"\u0044",
                    u"\u004b", u"\u004c", u"\u004d", u"\u0056", 
                    u"\u0058", u"\u0063", u"\u0064", u"\u0069", 
                    u"\u006a", u"\u006c", u"\u0076", u"\u0078"]
duplicate_code = [  u"\u2010", u"\u037e", u"\u216d", u"\u216e",
                    u"\u212a", u"\u216c", u"\u216f", u"\u2164",
                    u"\u2169", u"\u217d", u"\u217e", u"\u2170",
                    u"\u0458", u"\u217c", u"\u2174", u"\u2179"]

blank_space = [     u"\u0020", u"\u2000", u"\u2004", 
                    u"\u2005", u"\u2008", u"\u2009",
                    u"\u202f", u"\u205f"]

def getindex(str):
	for i in range(len(blank_space)):
		if blank_space[i]==str:
			return i

def getbinstr(num):
	num=bin(num)#0->'0b0',str
	num=num[2:]#->'0'
	lenn=len(num)
	num='0'*(3-lenn)+num#'000'
	#print(num)
	return num


def magic(wm):
	wm=reduce(lambda x,y:x+y,wm)#wm='0110'
	return wm

f=open('test_final.txt','rb')  #读模式打开
r = f.read( )   #bytes类型
f.close()

extract_org=r.decode('utf-8') #string类型



wm=['']#初始化，其实128个bit！！！！就够了，注意不是len(wm)

for m in range(len(extract_org)):
	#lenb=len(magic(wm))
	#print('lebwm=%d'%(lenb))
	#print(extract_org[m])
	#if lenb<130:
		if extract_org[m] in blank_space:
			#print('find space:%s'%(extract_org[m]))
			index=getindex(extract_org[m])#int
			#print(index)
			index=getbinstr(index)#str,'000'~'111'
			wm.append(index)
			#m+=2
			#for j in range(3):
				#wm.append(index[j])
		elif (extract_org[m] in original_code) | (extract_org[m] in duplicate_code):
			if extract_org[m] in original_code:
				#print('wm=0')
				wm.append('0')
			else:
				#print('wm=1')
				wm.append('1')
		else:
			continue
	#else:
		#break

wm.reverse()#eg,wm=['0','110']
wm=magic(wm)
wm2=wm[len(wm)-128:]
print(len(wm2))
print(wm2)







