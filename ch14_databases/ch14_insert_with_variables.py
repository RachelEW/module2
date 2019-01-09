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

#-----------------------------------------------#
"""Task Two: Add data to table with variables"""
#-----------------------------------------------#

import sqlite3 #importing SQLite toolkit
import time
import datetime
import random

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
    
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword,value)VALUES (?, ?, ?, ?)', (unix, date, keyword,value))
    conn.commit()
    
#create_table()
#data_entry()

#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)
#c.close()
#conn.close()


#-----------------------------------------------------------------#
"""Task Three: Reading and selecting data from a databas (p151)"""
#-----------------------------------------------------------------#

def read_from_db_all():
    c.execute('SELECT * FROM stuffToBuild WHERE value =8 ')
    for row in c.fetchall():
        print(row)
        
def read_from_db2():
    c.execute('SELECT * FROM stuffToBuild WHERE value =8 and unix > 1547028204 and unix < 1547029303 ')
    for row in c.fetchall():
        print(row[0])
        
#read_from_db_all()
read_from_db2()