#
#
#
#

import sys
from string import whitespace



def scan():
    typeMod = sys.argv[1]
    key = sys.argv[2]
    key = key.translate(None, whitespace)
    if(typeMod == "-e"):
        encode(key)

    elif (typeMod == "-d"):
        decode(key)

    else:
        print("Please enter -e or -d for encode or decode")
        exit()




def encode(k):
    while True:
        phrase = sys.stdin.readline()
        encString = ""
        keyIter = 0

        if(phrase == ""):
            exit()
        elif '\n' in phrase:
            phrase = phrase[:len(phrase)-1]
        
        for i in range(0, len(phrase)):
            isSymb = False
            isCapital = False


            if 'a' <= phrase[i] <= 'z':
                phInt = ord(phrase[i]) - 97
            elif 'A' <= phrase[i] <= 'Z':
                phInt = ord(phrase[i]) - 65
                isCapital = True
            elif phrase[i] == ' ':
                encString += ' '
                continue
            else:
                phInt = ord(phrase[i])
                isSymb = True

            if 'a' <= k[keyIter] <= 'z':
                keyInt = ord(k[keyIter]) - 97
            elif 'A' <= k[keyIter] <= 'Z':
                keyInt = ord(k[keyIter]) - 65
            else:
                print("Key contains non-alphabetical character.")
                exit()


            if keyIter >= len(k) - 1:
                keyIter = 0
            else:
                keyIter += 1

            if isSymb:
                encString += chr(phInt)
                keyIter -= 1
                if keyInt < 0:
                    keyInt = len(k) - 1

            elif isCapital:
                encString += chr(((phInt + keyInt) % 26) + 65)
            else:
                encString += chr(((phInt + keyInt) % 26) + 97)


        print(encString)

def decode(k):
    while True:
        phrase = sys.stdin.readline()
        decString = ""
        keyIter = 0

        if(phrase == ""):
            exit()
        elif '\n' in phrase:
            phrase = phrase[:len(phrase)-1]
        
        for i in range(0, len(phrase)):
            isSymb = False
            isCapital = False


            if 'a' <= phrase[i] <= 'z':
                phInt = ord(phrase[i]) - 97
            elif 'A' <= phrase[i] <= 'Z':
                phInt = ord(phrase[i]) - 65
                isCapital = True
            elif phrase[i] == ' ':
                decString += ' '
                continue
            else:
                phInt = ord(phrase[i])
                isSymb = True

            if 'a' <= k[keyIter] <= 'z':
                keyInt = ord(k[keyIter]) - 97
            elif 'A' <= k[keyIter] <= 'Z':
                keyInt = ord(k[keyIter]) - 65
            else:
                print("Key contains non-alphabetical character.")
                exit()


            if keyIter >= len(k) - 1:
                keyIter = 0
            else:
                keyIter += 1

            if isSymb:
                decString += chr(phInt)
                keyIter -= 1
                if keyInt < 0:
                    keyInt = len(k) - 1

            elif isCapital:
                decString += chr(((26 + phInt - keyInt) % 26) + 65)
            else:
                decString += chr(((26 + phInt - keyInt) % 26) + 97)


        print(decString)


if(len(sys.argv) >= 3):
    scan()


else:
    print("Too few arguments")

