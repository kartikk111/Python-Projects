# BMI Calculator
import math

weight = abs(float(input("Enter your weight in kilograms: ")))
height = abs(float(input("Enter your height in metres: ")))


BMI = float(round((weight)/((height)**2),2))

print("Your BMI is ",BMI)
if BMI <= 18.5:
    print("\nYou are underweight.")
elif BMI >= 18.5 and BMI <= 25:
    print("\nYou are healthy.")
else:
    print("You are overweight.")



