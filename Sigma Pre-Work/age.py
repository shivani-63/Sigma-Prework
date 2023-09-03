from datetime import datetime
import math

def converting_user_input():
    users_input = input('Please input a date in the format of YYYY/MM/DD:')
    date = datetime.strptime(users_input, "%Y/%m/%d")
    return date
#this function is converting the users input into a datetime object

def calculate_difference():
    date1 = converting_user_input()
    date2 = datetime.now()
    difference = str(date2 - date1)
    return difference 
#this function is calculating the difference between the users input and current date

def formatting_age():
    list_diff = (calculate_difference().split(' '))
    #splitting the difference value, as it gives difference in days, hours, minutes and seconds.
    days_int = int(list_diff[0])
    #index reference to the days part only
    days_to_years = (days_int/365.25)
    #converting days to years
    display_difference = print(f'The difference in years is {math.floor(days_to_years)}')
    return display_difference
#this function is formatting the values found from the calculate_difference() function.

formatting_age()
#call to final function, which pulls the previous two functions into call as well.