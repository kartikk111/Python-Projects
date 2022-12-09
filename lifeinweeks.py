# Program to calculate time left in life based on a study
import math

current_age = int(input("What is your current age? \t"))

print("If you were to live to 90 years of age...\n")

difference_age = int(90 - current_age)

months = int(difference_age * 12)

weeks = int(difference_age * 52)

days = int(difference_age * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

