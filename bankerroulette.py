import random

names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

print(names)
totalnames = len(names)
choice = random.randint(0, (totalnames-1))
billpayer = names[choice]

print(f"{billpayer} is going to buy the meal today!")