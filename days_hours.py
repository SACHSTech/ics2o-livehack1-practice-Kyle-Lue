number_of_hours = int(input("Enter the number of hours: "))
number_of_days = number_of_hours/24
number_of_hours_left = int(number_of_days) % 24
print ("The number of days is " + str(number_of_days) + " and the number of hours left is " + str(number_of_hours_left))
