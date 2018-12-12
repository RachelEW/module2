# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:49 2018

@author: 612383461
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode): #means if it is True
        if checkBalance(balance):
#            return ('Your balance is {}'.format(balance))
            if chooseTransaction() == '1':
                return 'You have choosen to perform a credit request'
            elif chooseTransaction() == '2':
                return 'You have choosen to purchase a data bundle'
            else:
                return 'Your request has not been recognised and the service cannot proceed'
        else:
            return 'Your balance is not sufficient: {}'.format(balance)
    else:
        return 'Wrong Password'#shows if password is False
#    print('not yet created')
    
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True
    else:
        return False
    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    
def chooseTransaction():
    print('''What would you like to do next?
Please choose a number from the following options:
        1. Credit balance request
        2. Purchase data bundle''')
    choice = input()
    if choice == '1':
        return '1'
    elif choice == '2':
        return '2'
    else:
        return 'You must choose one of the options listed above'