"""
-------------------------------------------------------------------------------
Name:   f_to_c.py
Purpose:  To change fahrenheit to celcius
 
Author: Lue.Kyle
 
Created:  08/02/2021
------------------------------------------------------------------------------
"""
print ("*****Farenheit to Celcius*****")
# Input Farenheit
fahrenheit = int(input("Input Farenheit degree measure: "))
# Calculate celcius
celcius = int((5/9)*(int(fahrenheit)-32))
#Output the result
print ("Celcius degree measure: " + str(celcius))