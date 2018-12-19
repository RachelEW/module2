# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:45:13 2018

@author: 612383461
"""

import ch03_rachel_functions
 
#---------------------------------------------------#
"""Task One and In Class Practice with User Input"""
#---------------------------------------------------#

ch03_rachel_functions.conversing_with_user()

#----------------------------------#
"""Task Two: Creating Functions"""
#----------------------------------#

ch03_rachel_functions.hello_world()
ch03_rachel_functions.my_name()

#--------------------------------------------#
"""Task Three: Using Range with Arguments"""
#--------------------------------------------#

ch03_rachel_functions.printing_list_using_range()

#-------------------------------------------------------------------#
"""In Class Practice: Calling a Function within another Function"""
#-------------------------------------------------------------------#

ch03_rachel_functions.write_name()
ch03_rachel_functions.hello_world2()
ch03_rachel_functions.adding_numbers()
ch03_rachel_functions.hello_world3()

#----------------------------------------------------------#
"""Task Three Continued: Adding Numbers using Arguments"""
#----------------------------------------------------------#

ch03_rachel_functions.add_two_numbers_from_args(5, 10)

#-------------------------------------------------#
"""In Class Practice: Functions with arguements"""
#-------------------------------------------------#
 
a1 = 'hello'
b1 = 'world'
a2 = 'love'
b2 = 'coding'
ch03_rachel_functions.hello_world_2args(a1, b1)
ch03_rachel_functions.hello_world_2args(a2, b2)


a3 = "Dogs"
b3 = "are"
c3 = "the"
d3 = "best!"
ch03_rachel_functions.hello_world_4args(a3, b3, c3, d3)

   
a4 = "Dogs"
b4 = "are"
c4 = "great"
ch03_rachel_functions.hello_world_3args(a4, b4, c4)

#----------------------------------------------#
"""Mid-Class Challenge: Distance Conversion"""
#----------------------------------------------#

ch03_rachel_functions.convert_distance_print(30)

returned_value1 = ch03_rachel_functions.convert_distance(35)
print (returned_value1, "\n")
    
#---------------------------------------#
"""Task Four: Temperature Conversion"""
#---------------------------------------#

ch03_rachel_functions.convert_temperature_print(10)

returned_value2 = ch03_rachel_functions.convert_temperature(20)
print (returned_value2)

temp_London = ch03_rachel_functions.convert_temperature(12)
print (temp_London)

#--------------------------------#
"""Task Five: Return Value"""
#--------------------------------#

returned_value = ch03_rachel_functions.add_two_numbers_and_return_value()
print (returned_value)
print(returned_value - 5)