#!/usr/bin/env python3
"""
    Program to demonstrate Basics of Input/Output
"""

# Importing Modules
import datetime

print(f"Min Year: {datetime.MINYEAR} | Max Year: {datetime.MAXYEAR}")

# Calculating the date
todays_date = datetime.datetime.now()
print(todays_date)
today = todays_date.strftime('%c')
print(today)

print(todays_date.strftime("%m/%d/%Y, %H:%M:%S"))