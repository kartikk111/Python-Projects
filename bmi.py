# BMI Calculator
import math
from PIL import Image

weight = abs(float(input("Enter your weight in kilograms: ")))
height = abs(float(input("Enter your height in metres: ")))

print(" \n\n       \033[1;3m BMI Ranges! ")

print("Underweight \t\t<18.5\nNormal range\t\t18.5 - 24.9\nOverweight\t\t\t25.0 - 29.9\nObese\t\t >= 30")
print("\tObese class I - \t30.0 — 34.9\n\tObese class II - \t\t35.0-39.9\n\tObese class III - \t\t>= 40\n\n")


#im = Image.open(r"E:\Python-Projects\bmichart.jpg")
#im.show()

BMI = float(round((weight)/((height)**2),2))

print("Your BMI is ",BMI)
if BMI <= 18.5:
    print("You are underweight.")
elif BMI >= 18.5 and BMI <= 25:
    print("You are healthy.")
else:
    print("You are overweight.")



