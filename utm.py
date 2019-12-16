#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Unicode Text Watermark Embedding Tool
# 
# author: evan, ly
# 
# 

import sys
import getopt
import hmac

from functools import reduce

embedment = 0
extraction = 0
file_path = "original_text.txt"
output_path = "watermarked_text.txt"

# confusable symbols: -, ;, C, D, K, L, M, V,
#                     X, c, d, i, j, l, v, s.

original_code =[u"\u002d", u"\u003b", u"\u0043", u"\u0044",
                u"\u004b", u"\u004c", u"\u004d", u"\u0056", 
                u"\u0058", u"\u0063", u"\u0064", u"\u0069", 
                u"\u006a", u"\u006c", u"\u0076", u"\u0078"]

duplicate_code=[u"\u2010", u"\u037e", u"\u216d", u"\u216e",
                u"\u212a", u"\u216c", u"\u216f", u"\u2164",
                u"\u2169", u"\u217d", u"\u217e", u"\u2170",
                u"\u0458", u"\u217c", u"\u2174", u"\u2179"]

trans = {   u"\u002d": u"\u2010", u"\u003b": u"\u037e",
            u"\u0043": u"\u216d", u"\u0044": u"\u216e",
            u"\u004b": u"\u212a", u"\u004c": u"\u216c",
            u"\u004d": u"\u216f", u"\u0056": u"\u2164",
            u"\u0058": u"\u2169", u"\u0063": u"\u217d",
            u"\u0064": u"\u217e", u"\u0069": u"\u2170",
            u"\u006a": u"\u0458", u"\u006c": u"\u217c",
            u"\u0076": u"\u2174", u"\u0078": u"\u2179"}



# whitespace symbols: Space, En quad, Three-per-em space,
#                     Four-per-em space, Punctuation space, Thin space,
#                     Narrow no-break space, Medium mathematical space.

blank_space = [ u"\u0020", u"\u2000", u"\u2004", 
                u"\u2005", u"\u2008", u"\u2009",
                u"\u202f", u"\u205f"]


def usage():
    print("Unicode Text Watermark Embedding Tool")
    print("----- Made By -----")
    print("Usage:")
    print("-e, --embed:     Embed watermark.")
    print("-h, --help:      View tool's manual.")
    print("-i, --input:     File to process.")
    print("-k, --key:       Key to generate watermark.")    
    print("-o, --output:    Save file to...")    
    print("-v, --help:      Please input Identity ID to verify.")
    print("-x, --extract:   Extract watermark.")
    print("----------- End of Manual -----------")

# get a whitespace index from blank_space
def getindex(str):
    for i in range(len(blank_space)):
        if blank_space[i] == str:
            return i

# joint strings in list
def magic(wm):
	wm = reduce(lambda x, y:x+y , wm) # wm = ['0110']
	return wm

# decimal to binary string
def getbinstr(num):
	num = bin(num)  # 0->'0b0', str
	num = num[2:]   #  ->'0'
	lenn = len(num)
	num = '0'*(3-lenn) + num #'000'
	return num

# watermark embedment
def embed(text_string, bitstream):
    chr_addr = 0
    bit_addr = 0
    bit_len = len(bitstream)
    text_watermarked = list(text_string)
    # print(len(text_string))
    # scan string for confusable character or blank space
    while(chr_addr < len(text_string)):
        # find a confusable character, read 1 bit from bitstream
        if text_watermarked[chr_addr] in original_code:
            # print("confusable char: %s" %(text_watermarked[chr_addr]))
            if(bitstream[bit_addr%bit_len] == '1'):
                text_watermarked[chr_addr] = trans[text_watermarked[chr_addr]]
            # print(bit_addr, bitstream[bit_addr%bit_len], text_watermarked[chr_addr])
            bit_addr = bit_addr + 1
        # find a blank space, read 3 bits from bitstream
        elif text_watermarked[chr_addr] in blank_space:
            # print("blank space: %s" %(text_watermarked[chr_addr]))
            # from bits to num
            temp = 4*int(bitstream[bit_addr%bit_len]) + 2*int(bitstream[(bit_addr+1)%bit_len]) + int(bitstream[(bit_addr+2)%bit_len])
            text_watermarked[chr_addr] = blank_space[temp]
            bit_addr = bit_addr + 3
        else:
            bit_addr = bit_addr
        # print(chr_addr, bit_addr)
        chr_addr = chr_addr + 1
    
    # print(text_string)
    # print(''.join(text_watermarked))
    return ''.join(text_watermarked)

# watermark extraction
def extract(text_watermarked):
    wm = ['']
    
    for ch in text_watermarked:
        if ch in blank_space:
            # print("find str:%s"%(ch))
            index = getindex(ch) # int
            index = getbinstr(index) # str,'000'~'111'
            wm.append(index)
        elif ch in original_code:
            wm.append('0')
        elif ch in duplicate_code:
            wm.append('1')
        else:
            continue

    # print("\n")
    # print(wm)
    return wm

def hash(value, key):
	hm = hmac.new(key, value)
	wm = hm.hexdigest( ) 
	str = ''
	for i in range(len(wm)):
		temp = bin(int((wm[i]), 16))
		temp = temp[2:]
		lent = len(temp)
		temp = '0'*(4-lent) + temp
		str = str + temp
	return str

def main():
    global file_path
    global output_path
    global embedment
    global extraction
    # if not len(sys.argv[1:]):
        # usage()
    
    # Read from comand line
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hexi:o:k:", ["help", "embed", "extract", "input", "output", "key"])
    except getopt.GetoptError as err:
        print(err)
        # usage()

    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-e", "--embed"):
            embedment = 1       
        elif o in ("-x", "--extract"):
            extraction = 1
        elif o in ("-i", "--input"):
            file_path = a
        elif o in ("-o", "--output"):
            output_path = a
        elif o in ("-k", "--key"):
            key = a        
        else:
            # assert False, "Unhanded Option"
            print("Unhandled Option")

    # temporary settings for test purpose
    # text_string = text_string.decode('utf-8')
    # text_string = "abcdedsiugxxxeusrigrxsixgjsxjgszznxaxcvrslkxxfodxxlxxi"
      
    
    # read from file(read only mode)
    f = open(file_path, 'rb')
    text_string = f.read()
    f.close()
    text_string = text_string.decode('utf-8')
    key = key.encode('utf-8')
    text = text_string.encode('utf-8')
    watermark = hash(text, key)

    if embedment:
        text_watermarked = embed(text_string, watermark)
        print(watermark)
        f2 = open(output_path, 'w+', encoding='utf-8')
        f2.write(text_watermarked)
        f2.close()
    elif extraction:
        watermark_extracted = extract(text_string)
        watermark_extracted = ''.join(watermark_extracted)
        print(watermark_extracted)
        # bitstram to hash
        #
        #
    else:
        print("unknown operation.")
    

main()
