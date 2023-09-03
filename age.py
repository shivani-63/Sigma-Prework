from datetime import datetime
import math

def calculate_difference(date_string):
    date1 = datetime.strptime(date_string, "%Y/%m/%d")
    date2 = datetime.now()
    difference = str(date2 - date1)
    return difference
#this function is calculating the difference between the users input and current date

def formatting_to_age(difference,date_string):
    list_diff = (calculate_difference(date_string).split(' '))
    #splitting the difference value, as it gives difference in days, hours, minutes and seconds.
    days_int = int(list_diff[0])
    days_to_years = (days_int/365.25)
    #converting days to years
    display_difference = (f'This birthdate ({date_string}) would make you {math.floor(days_to_years)} years old')
    return display_difference
#this function is formatting the values found from the calculate_difference() function.

test_cases = ['1990/08/31', '2000/03/06', '2013/09/04']

for test in test_cases:
    difference = calculate_difference(test)
    formatted_age = formatting_to_age(difference, test)
    print(formatted_age)
