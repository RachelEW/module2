# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:38:51 2019

@author: winkl
"""

#####################################################
"""Creating functions to count words in a document"""
#####################################################

###############################
"""Task One: Counting Words"""
###############################

my_file=open("mobydick.txt","r")
moby = (my_file.read())

#with open("mobydick.txt") as file:
#    moby=file.read()

lines = []
words = []

def createListWords(filename):
    for line in filename.split('\n'):
        lines.append(line)
#    print(lines)
    for i in range(len(lines)):
        a_line = lines[i]
#        print(a_line)
        for word in a_line.split(' '):
            words.append(word)
    words.remove('' '')
    return words
    
def countListWords(given_list):
    counts = {}
    for word in given_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
    

createListWords(moby)
countListWords(words)

#
###Chen's Example
#def countWords(filename):
#    counts = {}
#    info = open(filename,'r')
#    for line in info:
#        words = line.split()
#        for word in words:
#            if word in counts:
#                counts[word] += 1
#            else:
#                counts[words] = 1
#    return counts
#
#countWords(mobydick.txt)


###################################
"""Task Two: Sorting and Ranking"""
###################################

def printTop20():
    counts.