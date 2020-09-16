#!/usr/bin/env python3
"""
    Program to demonstrate Basics of Input/Output
"""

name = input('Enter your name: ')
age = int(input('Enter your age: '))
salary = float(input('Enter your Salary: '))
is_manager = bool(int(input("Enter Manager Status (0/1): ")))

print("====================================================")
print("******************** Employee Details ********************")
print("====================================================")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Salary: {salary}")
print(f"Is Manager: {is_manager}")


print("----------------------------------------------------")