#function: evaluation when len(test_watermark)<128
#input:test_wm
#output:similarity rate
#author:ly

import math


test=0b00100101101
wm=0b00101101011000111000100010011111101011001101000101011000111101110100100010011101100011111001000101100110011011101000111001001001



#异或，比相减快
def issame(int1,int2):
	a=xor(int1,int2)
	if a == 0:
		return 1
	else:
		return 0
#得到 int 形式的测试水印test，原始水印wm

#
lent=len(test)#eg.63
a=math.floor(math.log(x,2))#向下取整,5
split=lent;#分片大小，比较的基本单元,63,2^^5,2^^4,2^^3,2^^2,2^^1

hit=0;#相等的次数
count=0;#一种分片下，比较的总次数
result=0#输出的比率

while(split > 2):
	for i in range(0,128-split):
		for j in range(0,lent-split):
			count+=1
			m=wm[i:i+split+1]
			n=test[j:j+split+1]
			hit+=issame(m,n)
	if split == lent:
		rate =1;#权重初值为1
		p=math.floor(math.log(split,2))
		if split %2 ==0:
			split = 2^^(p-1)
		else:
			split = 2^^(p)
	else :#第二次分片开始
		split/=2
		rate /=2
	result+=rate*(hit/count)

print(resut)











