# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:49 2018

@author: 612383461
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode): #means if it is True
        return 'Password OK'
    else:
        return ' Wrong Password'#shows if password is False
#    print('not yet created')
    
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True
    else:
        return False