# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:19:57 2019

@author: winkl
"""

#################
"""Databases"""
#################

#-----------------------#
"""Using MySQLite"""
#-----------------------#

#----------------------------------#
"""Task One: Creating a Database"""
#----------------------------------#

import sqlite3 #importing SQLite toolkit

conn = sqlite3.connect('task1.db') #as we are creating te database we can just name the database fie with .db at the end
c = conn.cursor() #conenct to cursor, low level pointer specifically used in databases to find positions of data in each data table

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL , datestamp TEXT, keyword TEXT, value REAL)")
    
#NB: 'CREATE TABLE IF NOT EXISTS' is the command to create and check the existance of a table

def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(12233222, '2018-01-1', 'python', 5)")
    conn.commit() #running commit command after inserting values into a database
    c.close()
    conn.close()
    
create_table()
data_entry()