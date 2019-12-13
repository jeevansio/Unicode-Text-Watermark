# -*- coding: utf-8 -*-
# confusable symbols: -, ;, C, D, K, L, M, V,
#                     X, c, d, i, j, l, v, s.
#此代码实现utf-8，而暂不先考虑文本用其他编码
#ly

#import chardet
import hmac

passwd=b'20173015'
original_code = [   u"\u002d", u"\u003b", u"\u0043", u"\u0044",
                    u"\u004b", u"\u004c", u"\u004d", u"\u0056", 
                    u"\u0058", u"\u0063", u"\u0064", u"\u0069", 
                    u"\u006a", u"\u006c", u"\u0076", u"\u0078"]

'''duplicate_code = [u"\u2010", u"\u037e", u"\u216d", u"\u216e",
                    u"\u212a", u"\u216c", u"\u216f", u"\u2164",
                    u"\u2169", u"\u217d", u"\u217e", u"\u2170",
                    u"\u0458", u"\u217c", u"\u2174", u"\u2179"] '''

duplicate_code2={    u"\u002d":u"\u2010",u"\u003b":u"\u037e",
    				 u"\u0043":u"\u216d",u"\u0044":u"\u216e",
    				 u"\u004b":u"\u212a",u"\u004c":u"\u216c",
    				 u"\u004d":u"\u216f",u"\u0056":u"\u2164",
    				 u"\u0058":u"\u2169",u"\u0063":u"\u217d",
    				 u"\u0064":u"\u217e",u"\u0069":u"\u2170",
    				 u"\u006a":u"\u0458",u"\u006c":u"\u217c",
    				 u"\u0076":u"\u2174",u"\u0078":u"\u2179"}


def myhash(value,key):
	hm = hmac.new(key,value)
	wm = hm.hexdigest( ) 
	str=''
	for i in range(len(wm)):
		temp=bin(int((wm[i]),16))
		temp=temp[2:]
		lent=len(temp)
		temp='0'*(4-lent)+temp
		str=str+temp
	return str


# whitespace symbols: Space, En quad, Three-per-em space,
#                     Four-per-em space, Punctuation space, Thin space,
#                     Narrow no-break space, Medium mathematical space.

blank_space = [u"\u0020", u"\u2000", u"\u2004", 
                u"\u2005", u"\u2008", u"\u2009",
                u"\u202f", u"\u205f"]


f=open('test_embed.txt','rb')  #读模式打开
r = f.read( )   #bytes类型
f.close()
watermark=myhash(r,passwd)
print(watermark)

original_text=r.decode('utf-8') #string类型
#print(original_text)
f3=open('test_original.txt','w+')
f3.write(original_text)
f3.close()

text_string=original_text

wm=list(watermark)
#需要进一步初始化wm使其足够pop
for j in range(128):
	wm[j]=ord(wm[j])-ord('0')
#转换成1，0，...整数
#print(wm)
count=0
for ch in text_string:
	count+=1
wm=wm*(count//128+1)





text_string = list(text_string)
for k in range(len(text_string)):
	if text_string[k] in original_code:
		print('find ch:%s'%(text_string[k]))
		a=wm.pop()
		if a == 1:
			text_string[k] = duplicate_code2[text_string[k]]
		else:
			continue
	elif text_string[k] in blank_space:
		print('find space:%s'%(text_string[k]))
		a=wm.pop()+2*wm.pop()+4*wm.pop()
		text_string[k] = blank_space[a])
		k+=2
	else:
		pass
text_string = ''.join(text_string)
f2=open('test_final.txt','w+',encoding='utf-8')
f2.write(text_string)
f2.close()












