#
#
#
#

import sys



def scan():
    typeMod = sys.argv[1]
    key = sys.argv[2]

    if(typeMod == "-e"):
        # ty = 0
        encode(key)

    elif (typeMod == "-d"):
        # ty = 1
        decode(key)

    else:
        # ty = -1
        print("Please enter -e or -d for encode or decode")
        exit()




def encode(k):
    while True:
        phrase = sys.stdin.readline()
        encString = ""
        keyIter = 0

        if(phrase == ""):
            exit()
        k = k.replace('\n', '')
        k = k.replace('\t', '')
        k = k.replace('\n', '')

        # for i in range(0, len(phrase)):
            # if(
        
        for i in range(0, len(phrase)):
            keyIndex = i % len(k)
            currKey = k[keyIndex]
            currPh = phrase[keyIndex]
            # encString += chr((int(currKey) + int(currPh)) % 64)

            \

def decode(k):
    while True:



if(len(sys.argv) >= 3):
    scan()


else:
    print("Too few arguments")

