# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:22:45 2018

@author: winkl
"""

#############################
"""While Loops"""
#############################

x = 33
while x >= 1:
    print(x, ': ', end='') #end='' adds a space at the end
    x = x / 2
print(x)

#------------------#
"""Exercise 1: Computing triangular numbers"""
#------------------#

def generateTriangularNo(n):
    triangularSum = 0
    while n >= 1:
        triangularSum = triangularSum + n
        n = n-1
    return(triangularSum)
    
triangularSum1 = generateTriangularNo(4)
print(triangularSum1)

#-----------------#
"""Exercise 2: Determining if a student has passed or failed"""
#-----------------#
def generateGrade():
    counter = 0
    mark = 0
    averageMark = 0
    while counter < 6:
        mark = input("What mark did the student achieve in the test? ")
        mark = int(mark)
        counter += 1
        averageMark = (averageMark + mark) / 2
        if averageMark >= 70:
            print("Grade: First Class")
        elif averageMark >= 40:
            print("Grade: Pass")
        else:
            print("Grade: Fail")
    print("Average Mark: ", averageMark)

###TEST###
#generateGrade()

#----------------------#
"""Using a break statement to exit a while loop"""
#----------------------#

i = 55
while i > 10:
    print(i)
    i = i*0.
    if i == 35.2:
        break

#---------------------#
"""Exercise 3: Greeting until user is done"""
#---------------------#

def greet():
    name = input("What is your name? ")
    while name != "done":
        print("Hello,", name, "nice to meet you!")
        name = input("""What is your name?
Or print 'done' if you would like to exit the greeting generator. """)
    print("Thank you for using the greeting generator. Goodbye.")
    
###TEST###
#greet()

#OR an alternative...#

def greet2():
    while True:
        name = input("Enter name: ")
        if name == "done":
            break
        print("Hello", name)
        
###TEST###
greet2()