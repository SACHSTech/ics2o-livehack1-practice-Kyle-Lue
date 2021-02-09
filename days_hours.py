"""
-------------------------------------------------------------------------------
Name:   days_hours.py
Purpose:  To determine the number of days and hours from inputing the hours
 
Author: Lue.Kyle
 
Created:  date in 08/02/2021
------------------------------------------------------------------------------
"""
#Input the hours
number_of_hours = int(input("Enter the number of hours: "))
#Calculate the result
number_of_days = number_of_hours//24
number_of_hours_left = int(number_of_hours) % 24
#Output the result
print ("The number of days is " + str(number_of_days) + " and the number of hours left is " + str(number_of_hours_left))
