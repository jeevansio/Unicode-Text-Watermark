#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt

def usage():
    print("Unicode Text Watermark Embedding Tool")
    print("\n")
    print("\n")
    print("\n")
    print("\n")    
    print("\n")
    print("\n")    
    print("\n")
    print("\n")


def main():
    
    global text
    global file_path
    global text_output
    global output_path


    if not len(sys.argv[1:]):
        usage()
    
    # Read from comand line
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:f:T:F:", ["help", "text", "file", "TEXT", "FILE"])
    except getopt.GetoptError as err:
        print(err)
        usage()

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
    
#usage()
main()