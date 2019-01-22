# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:01:16 2019

@author: winkl
"""

import config

###################################
"""Task One: APIs using Mailgun"""
###################################

import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd69fab2e492a46c28c5bbbef9404f202.mailgun.org",
        auth=("api", config.mailgun_api_key),
        data={"from": "Rachel Winkler <rachelwinkler9@gmail.com>",
              "to": ["rachel.winkler@hotmail.com", "rachel.winkler@hotmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
    
send_simple_message()