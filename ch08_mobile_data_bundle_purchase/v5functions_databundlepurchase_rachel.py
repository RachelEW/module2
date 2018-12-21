# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:49 2018

@author: 612383461
"""

#####################################################
"""Creating a Mobile Data Bundle Purchase Program"""
#####################################################

#-----------------------------------------------------#
"""Use of subfunctions to make code cleaner
Adding three password attempts"""
#-----------------------------------------------------#

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode): #means if it is True
            transactionType = chooseTransaction()
            if transactionType =='1':
                if checkBalance(balance):
                    return 'Your balance is £{}'.format(balance)
                else:
                    return 'Your balance is not sufficient: £{}'.format(balance)
            elif transactionType =='2':
                stepsForDataBundlePurchase(balance)
            else:
                return 'Your request has not been recognised and the service cannot proceed, please try logging in again.'
    return 'Thank you for using our online system.'

#---Conducting password checks---#
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True
    else:
        if passwordCheckTwo(truePasscode):
            return True
        else:
            if passwordCheckThree(truePasscode):
                return True
            else:
                print('You have entered your password incorrectly three times. Please reset your password.')
                return False
    
def passwordCheckTwo(truePasscode):
    print('''\nThe password you have entered is not correct, please try again.
You have 2 attempts left.''')
    attempt2 = input()
    if attempt2 == truePasscode:
        return True
    else:
        return False
    
def passwordCheckThree(truePasscode):
    print('''\nThe password you have entered is not correct, please try again.
You have 1 attempt left.''')
    attempt3 = input()
    if attempt3 == truePasscode:
        return True
    else:
        return False

#---Checking Balance---#
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False

#---Choosing Transation---#
def chooseTransaction():
    print('''\nWhat would you like to do next?
\nPlease choose a number from the following options:
        1. Credit balance request
        2. Purchase data bundle''')
    transactionType = input()
    return transactionType

#---Steps for purchasing Data Bundle---#
def stepsForDataBundlePurchase(balance):
    if choosingPhoneNumber():
        if purchaseDataBundle(balance):
            return 'Thank you for purchasing a data bundle!'
        else:
            return 'Data bundle purchase was unsuccessful, please try logging in again.'

#---Supplying phone number for purchases---#
def choosingPhoneNumber():
    phoneNo = inputPhoneNumber()
    lengthPhoneNo = checkLengthPhoneNumber(phoneNo)
    if lengthPhoneNo == 11:
        if validatePhoneNumber(phoneNo):
            print('\nThank you for confirming your phone number. Please try logging in again.')
            return True
        else:
            print('\nThe phone numbers you entered do not match. Please try logging in again.')
            return False
    else:
        print('\nYour phone number must be 11 digits long. Please do not include the country code. Please try logging in again.')
        return False

def inputPhoneNumber():
    print('\nPlease input your phone number:')
    phoneNoAttempt = input()
    return phoneNoAttempt

def checkLengthPhoneNumber(phoneNo):
    lengthPhoneNo = len(phoneNo)
    return lengthPhoneNo

def validatePhoneNumber(phoneNo):
    print('''\nThank you, please repeat your phone number to complete confirmation:''')
    secondPhoneNoAttempt = input()
    if secondPhoneNoAttempt == phoneNo:
        return True
    else:
        return False

#---Purchasing a data bundle---#
def purchaseDataBundle(balance):
    purchaseAmount = checkDataBundlePurchaseAmount(balance)
    if (balance - purchaseAmount) >= 0:
        if checkMaxPurchaseAmount(purchaseAmount):
            if multipleof5PurchaseAmount(purchaseAmount):
                print('\nThank you for purchasing a data bundle with a value of £{}. Your new bundle has been added to your phone!'.format(purchaseAmount))
                return True
            else:
                print('\nYou can only purchase a data bundle with a value which is a multiple of £5.')
                return False
        else:
            print('\nYou cannot purchase a data bundle with a value which exceeds £50.')
            return False
    else:
        print('\nYou do not have enough credit to make this purchase. Your balance is £{}.'.format(balance))
        print('Data bundle purchase was unsuccessful, please try logging in again.')
        return False

def checkDataBundlePurchaseAmount(balance):
    print('''\nYou may purchase a data bundle up to the value of the balance which you have in your account and up to a maximum of £50. The purchase amount must be a multiple of £5.
\nHow much would you like to spend to purchase a data bundle?''')
    purchaseAmount = int(input())
    return purchaseAmount
    
def checkMaxPurchaseAmount(purchaseAmount):
    if purchaseAmount <= int(50):
        return True
    else:
        return False

def multipleof5PurchaseAmount(purchaseAmount):
    if purchaseAmount % 5 == 0:
        return True
    else:
        return False