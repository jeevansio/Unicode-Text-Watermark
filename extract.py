#author:ly
#function:extract wm
#note that this doesn't worl,the output wm is 00000... which is obviously wrong
#I doubt that is due to the type error when transforming and I'm trying to fix it,welcome solutions

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
	return num
def magic(wm):
	wm=reduce(lambda x,y:x+y,wm)#wm=['0110']
	return wm

f=open('test_final.txt','rb')  #读模式打开
r = f.read( )   #bytes类型
f.close()

extract_org=r.decode('utf-8') #string类型



wm=['']#初始化，其实128个元素就够了

for ch in extract_org:
	if len(wm)<128:
		if ch in blank_space:
			print('find str:%s'%(ch))
			index=getindex(ch)#int
			index=getbinstr(index)#str,'000'~'111'
			wm.append(index)
			#for j in range(3):
				#wm.append(index[j])
		elif (ch in original_code) | (ch in duplicate_code):
			if ch in original_code:
				wm.append('0')
			else:
				wm.append('1')
		else:
			continue
	else:
		break

wm.reverse()#eg,wm=['0','110']
wm=magic(wm)
print(wm)







