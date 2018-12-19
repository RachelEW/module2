# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:49 2018

@author: 612383461
"""

#####################################################
"""Creating a Mobile Data Bundle Purchase Program"""
#####################################################

#------------------------------------#
"""Before Adding More SubFunctions"""
#------------------------------------#

def DataBundlePurchase(truePasscode, balance, phoneNumber):
    if passwordCheck(truePasscode): #means if it is True
        if checkBalance(balance):
            transactionType = chooseTransaction()
#            print('out')
            if transactionType =='1':
                if checkBalance(balance):
                    return 'Your balance is {}'.format(balance)
                else:
                    return 'Your balance is not sufficient: {}'.format(balance)
            elif transactionType =='2':
                phoneNoAttempt = inputPhoneNumber()
                lengthPhoneNo = checkLengthPhoneNumber(phoneNoAttempt)
                if lengthPhoneNo == 11:
                    if validatePhoneNumber(phoneNoAttempt):
                        purchaseAmount = checkDataBundlePurchaseAmount(balance)
                        if (balance - purchaseAmount) >= 0:
                            if checkMaxPurchaseAmount(purchaseAmount):
                                if multipleof5PurchaseAmount(purchaseAmount):
                                    return 'Thank you for purchasing a data bundle with a value of £{}. Your new bundle has been added to your phone!'.format(purchaseAmount)
                                else:
                                    return 'You can only purchase a data bundle of a value which is a multiple of £5. Please try logging in again.'
                            else:
                                return 'You cannot purchase a data bundle with a value which exceeds £50, please try logging in again.'
                        else:
                            return 'You do not have enough credit to make this purchase. Your balance is {}. Please try logging in again to make a purchase.'.format(balance)
                    else:
                        return 'The phone number you entered does not match, please try logging in again.'
                else:
                    return 'Your phone number must be 11 digits long. Please do not include the country code.'
            else:
                return 'Your request has not been recognised and the service cannot proceed, please try logging in again.'
        else:
            return 'Your balance is not sufficient to perform any transactions: {}'.format(balance)
    else:
        return 'You have entered your password incorrectly three times. Please reset your password.'
    
#Conducting password checks
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

#Checking Balance
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False

#Choosing Transation
def chooseTransaction():
    print('''\nWhat would you like to do next?
\nPlease choose a number from the following options:
        1. Credit balance request
        2. Purchase data bundle''')
    transactionType = input()
    return transactionType

#Confirming phone number for purchases
def inputPhoneNumber():
    print('\nPlease input your phone number:')
    phoneNoAttempt = input()
    return phoneNoAttempt

def checkLengthPhoneNumber(phoneNoAttempt):
    lengthPhoneNo = len(phoneNoAttempt)
    return lengthPhoneNo

def validatePhoneNumber(phoneNoAttempt):
    print('''\nThank you, please repeat your phone number to complete confirmation:''')
    secondPhoneNoAttempt = input()
    if secondPhoneNoAttempt == phoneNoAttempt:
        return True
    else:
        return False

#Purchasing a data bundle
def checkDataBundlePurchaseAmount(balance):
    print('''\nThank you for confirming your phone number.
\nYou may purchase a data bundle up to the value of the balance which you have in your account and up to a maximum of £50. The purchase amount must be a multiple of £5.
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