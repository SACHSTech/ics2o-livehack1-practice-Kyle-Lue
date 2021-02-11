number_of_minutes = int(input("Enter the number of minutes: "))
number_of_days = number_of_minutes//1440
remaining_minutes = minutes%1440
hours = remaining_minutes//60
final_minutes = remaining_minutes - hours*60

print ("The number of days is " + str(number_of_days) + " the number of hours left is " + str(number_of_hours) + " the number of minutes are" + str(number_of_minutes))
