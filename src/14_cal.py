"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.

 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.

 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.

 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

month = datetime.now().month
year = datetime.now().year

# Check in the following order if:
# - an incorrect number of arguments is entered
# - inputed month is between 1 and 12
# - inputed year is between 1 and 9999
# - inputed month is an integer
# - inputed year is an integer
if (len(sys.argv) > 3 or (not 1 <= int(sys.argv[1]) <= 12) or (not 1 <= int(sys.argv[2]) <= 9999) or (not isinstance(month, int)) or (not isinstance(year, int))):
    print(f"**Input Error**\n\nPlease enter the month and year as arguments in the following format `MM YYYY` \nor `MM` to get the calendar for the current year. \n\nExample 1: \"9 1999\" will show you the calendar for September 1999\nExample 2: \"1\" will show you the calendar for January {year}\n")
    sys.exit()

if len(sys.argv) > 1:
    month = int(sys.argv[1])
    year = year

if len(sys.argv) > 2:
    month = int(sys.argv[1])
    year = int(sys.argv[2])

def calendarize(month = month, year = year):
  print(calendar.month(year, month))

calendarize(month, year)