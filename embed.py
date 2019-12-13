#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt
import bitarray
import hmac


#input: value='iloveu',key=(passwd)=(identification)=b'20173015',both type=bytes
#output:type=str,len=128,eg='101010101...'
def myhash(value,key):
	hm = hmac.new(key,value)
	wm = hm.hexdigest( ) 
	#print(wm)
	#len=32,str,hex,eg"5157f56c40e7d4964bf9bca8e4fb9a63"
	str=''
	for i in range(len(wm)):
		temp=bin(int((wm[i]),16))
		temp=temp[2:]
		lent=len(temp)
		temp='0'*(4-lent)+temp
		str=str+temp
	#print(str)
	#print(len(str))
	return str

def usage():
    print("Unicode Text Watermark Embedding Tool")
    print("\n"*8)


def main():
    
    global text
    global file_path
    global text_output
    global output_path

    global watermark_bitstream
    global text_string

    # if not len(sys.argv[1:]):
        # usage()
    
    # Read from comand line
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:f:T:F:", ["help", "text", "file", "TEXT", "FILE"])
    except getopt.GetoptError as err:
        print(err)
        # usage()

    for o,a in opts:
        if o in ("-h", "--HELP"):
            usage()
        elif o in ("-t", "--text"):
            text = a
        elif o in ("-f", "--file"):
            file_path = a
        elif o in ("-T", "--TEXT"):
            text_output = a
        elif o in ("-F", "--FILE"):
            output_path = a
        else:
            # assert False, "Unhanded Option"
            print("Unhandled Option")
    
    # confusable symbols: -, ;, C, D, K, L, M, V,
    #                     X, c, d, i, j, l, v, s.

    original_code = [u"\u002d", u"\u003b", u"\u0043", u"\u0044",
                    u"\u004b", u"\u004c", u"\u004d", u"\u0056", 
                    u"\u0058", u"\u0063", u"\u0064", u"\u0069", 
                    u"\u006a", u"\u006c", u"\u0076", u"\u0078"]

    duplicate_code = [u"\u2010", u"\u037e", u"\u216d", u"\u216e",
                    u"\u212a", u"\u216c", u"\u216f", u"\u2164",
                    u"\u2169", u"\u217d", u"\u217e", u"\u2170",
                    u"\u0458", u"\u217c", u"\u2174", u"\u2179"]

    # whitespace symbols: Space, En quad, Three-per-em space,
    #                     Four-per-em space, Punctuation space, Thin space,
    #                     Narrow no-break space, Medium mathematical space.

    blank_space = [u"\u0020", u"\u2000", u"\u2004", 
                u"\u2005", u"\u2008", u"\u2009",
                u"\u202f", u"\u205f"]


    # for symbol in original_code:
    #     print (symbol)
    # for i in duplicate_code:
    #     print(i)
    #print(text)


    # text_string = open(file_path, encoding='utf-8')
    f=open(r'D:\embed\test_embed.txt','rb')  #二进制读模式打开
    r = f.read( ) #bytes
    text_string=r.decode('utf-8')     #string
    original_text = text_string   
    f.close()
    watermark=myhash(r,passwd) #已经测试过这样可以得到正确的比特串，type=str,len=128
	

    #text_string = "abcd edsiugxxxeusrig rsigjsjgseigsli"
    bitstream=watermark
    #bitstream = b"01010010101010"
    bit_addr = 0
    txt_addr = 0
    bit_len = len(bitstream)#128

    while(txt_addr < len(text_string)):
        for i in range(16):
            if text_string[txt_addr] == original_code[i]:
                print(text_string[txt_addr], original_code[i])
                text_string = text_string.replace(text_string[txt_addr], duplicate_code[i])
                bit_addr = bit_addr + 1
        for i in range(8):
            if text_string[txt_addr] == blank_space[i]:
                print(text_string[txt_addr], blank_space[i])
                text_string = text_string.replace(text_string[txt_addr], blank_space[i])
                bit_addr = bit_addr + 3
        print(bitstream[bit_addr%bit_len], bit_addr)                
        txt_addr = txt_addr + 1

    print(text_string)
    print(original_text)
#usage()
main()
