#function: evaluation when len(test_watermark)<128
#input:test_wm
#output:similarity proportion
#author:ly

import math

#得到 str 形式的测试水印test，原始水印wm
#eg.test=wm[1:],其实相当于这个算法的最完美匹配，期待其输出接近100%，作为归一化的标准
test='010110101100011100010001001111110101100110100010101100011\
1101110100100010011101100011111001000101100110011011101000111001001001'
wm='0010110101100011100010001001111110101100110100010101100011\
1101110100100010011101100011111001000101100110011011101000111001001001'

def issame(str1,str2):
	if str1 == str2:
		return 1
	else:
		return 0


#输入位数<128
lent=len(test)#eg.63
a=math.floor(math.log(lent,2))#向下取整,5
split=lent;#分片大小，比较的基本单元,63,2^^5,2^^4,2^^3,2^^2,2^^1
#count_sum=0#一种分片下，比较的总次数
result=0#输出的比率

while(split > 2 and split <128):
	split=int(split)
	hit=0#每次分片相等的次数
	count_tem=0
	for i in range(0,128-split):
		for j in range(0,lent-split+1):
			count_tem+=1
			m=wm[i:i+split+1]
			n=test[j:j+split+1]
			hit+=issame(m,n)
	if split == lent:
		rate =1;#权重初值为1
		p=math.floor(math.log(split,2))
		if split %2 ==0:
			split = 2**(p-1)
		else:
			split = 2**(p)
	else :#第二次分片开始
		split/=2
		rate /=2
	#count_sum+=count_tem
	result+=rate*(hit/count_tem)*75
	print('hit=%d'%(hit))
	print('rate=%f'%(rate))
	print('resut_tem=%f'%(result))

#print('\n 扩幅参数=%d'%(k))
print('\nresult=%f'%(result))
#print('count_sum=%d'%(count_sum))










