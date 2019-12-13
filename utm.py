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

embedment = 0
extraction = 0
file_path = ""
output_path = ""

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

detrans = { u"\u2010": u"\u002d", u"\u037e": u"\u003b",
            u"\u216d": u"\u0043", u"\u216e": u"\u0044",
            u"\u212a": u"\u004b", u"\u216c": u"\u004c",
            u"\u216f": u"\u004d", u"\u2164": u"\u0056",
            u"\u2169": u"\u0058", u"\u217d": u"\u0063",
            u"\u217e": u"\u0064", u"\u2170": u"\u0069",
            u"\u0458": u"\u006a", u"\u217c": u"\u006c",
            u"\u2174": u"\u0076", u"\u2179": u"\u0078"}

# whitespace symbols: Space, En quad, Three-per-em space,
#                     Four-per-em space, Punctuation space, Thin space,
#                     Narrow no-break space, Medium mathematical space.

blank_space = [ u"\u0020", u"\u2000", u"\u2004", 
                u"\u2005", u"\u2008", u"\u2009",
                u"\u202f", u"\u205f"]


def usage():
    print("Unicode Text Watermark Embedding Tool")
    print("\n"*8)

def embed(text_string, bitstream):
    bit_addr = 0
    bit_len = len(bitstream)

    # scan string for confusable character or blank space
    for character in text_string:
        # find a confusable character, read 1 bit from bitstream
        if character in original_code:
            print("confusable char: %s" %(character))
            if(bitstream[bit_addr%bit_len] == "1"):
                character = trans[character]
            print(bitstream[bit_addr%bit_len], character)
            bit_addr = bit_addr + 1
        # find a blank space, read 3 bits from bitstream
        elif character in blank_space:
            print("blank space: %s" %(character))
            temp = 4*bitstream[bit_addr%bit_len] + 2*bitstream[(bit_addr+1)%bit_len] + bitstream[(bit_addr+2)%bit_len]
            character = blank_space[temp]
            bit_addr = bit_addr + 3
        else:
            continue

    print(text_string)
    return text_string

def extract():
    print("\n")

def hash(value, key):
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
        if o in ("-h", "--HELP"):
            usage()
        elif o in ("-i", "--input"):
            embedment = 1       
        elif o in ("-i", "--input"):
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
    file_path = "original_text.txt"
    output_path = "watermarked_text.txt"
    text_string = open(file_path)
    text_string = text_string.read()
    # text_string = text_string.decode('utf-8')
    # text_string = "abcdedsiugxxxeusrigrxsixgjsxjgszznxaxcvrslkxxfodxxlxxi"
    watermark = list("01")

    if embedment:
        text_watermarked = embed(text_string, watermark)
        f2 = open(output_path, 'w+')
        f2.write(text_watermarked)
        f2.close()
    elif extraction:
        extract()
    

main()
