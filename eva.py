#function: evaluation when len(test_watermark)<128
#input:test_wm
#output:similarity proportion
#author:ly

import math

# test only
#得到 str 形式的测试水印test，原始水印wm
#eg.test=wm[1:],其实相当于这个算法的最完美匹配，期待其输出接近100%，作为归一化的标准
# '''test='0010110101100011100010001001111110101100110100010101100011\
# 1101110100100010011101100011111001000101100110011011101000111001001001'''
# wm='0010110101100011100010001001111110101100110100010101100011\
# 1101110100100010011101100011111001000101100110011011101000111001001001'
# wm2='101011000000111011100001101101100111011111101101101111000\
# 10101111100001000010110010111110100000001010100000110000101011010010111'
# wm3='0000011100011011101101001011000111100111000010010100100110010101\
# 0110110111111101010001010001000010000000110101100010100110000110'
# wm4='100001101010110111101101110100000101101000110011010111001101011100\
# 10110011001110111001111111111111011111000011011101011001000100'
# a=80
# test=wm4[a:]



def issame(str1,str2):
	if str1 == str2:
		return 1
	else:
		return 0

def cmp_wm(wm, test):
	a=80
	test=wm[a:]
	#输入位数<128
	lent=len(test)#eg.63
	a=math.floor(math.log(lent,2))#向下取整
	if a >6  or a <1:
		print('input test_wm bitlen∈（6,128）\n')
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
			rate=1-0.2*(6-a)#a>=1时有效，也就是test_bit>=2时有效
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
	return result

def xor_bin(str1, str2):
	count = 0
	if len(str1) == len(str2):
		for i in range(0, len(str1)-1):
			if str1[i] == str2[i]:
				count += 1
		return count/len(str1)
	else:
		return 100000


def cmp_wm_t(wm, test):
	len_w = len(wm)
	len_t = len(test)
	wm2 = wm + wm
	p = 0
	m = 0
	n = 0
	print("oooo")
	if len_w <= len_t:
		for j in range(0, len_t-128):
			for i in range(0, len_w - 1):
				m = xor_bin(wm2[i:i+127], test[j:j+127])
				if m >= n:
					n = m
			if n >= p:
				p = n
		return p
	else:
		result = cmp_wm(wm, test)
		return result









