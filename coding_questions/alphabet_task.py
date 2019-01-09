# -*- coding: utf-8 -*-

#########################################################

"""1. Write the letters 'A' to 'Z' (in upper case) to the console, placing each letter on a new line.

2. For every third letter, write it to the console in lowercase instead

3. For every fourth letter, write its numeric position in the alphabet to the console instead
(e.g. instead of outputting 'D' output '4').

4. If a letter satisfies both rules 2 and 3, write out its numeric position follwoed by the letter in lowercase
(e.g. 'L' should be output as '12l')."""

#########################################################

import string
alphabet = list(string.ascii_uppercase)

for i in range(len(alphabet)):
    if (i+1) % 3 == 0 and (i+1) % 4 == 0:
        print(str(i+1)+alphabet[i].lower())
    elif (i+1) % 3 == 0 :
        print(alphabet[i].lower())
    elif (i+1) % 4 == 0:
        print(i+1)   
    else:
        print(alphabet[i])