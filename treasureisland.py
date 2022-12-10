#Little Treasure Island game (nested if-else practice)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You're at a crossroads, enter your choice: left or right. \t").lower()

if choice == "left":
    choice1 = input("You reached a lake and there's crocodiles in it, enter your decision: swim or wait.\n").lower()
    if choice1 == "wait":
        choice2 = input("Three colored magical doors appeared in front of you: Red, Blue and Yellow. Choose one of the three to win\n").lower()
        if choice2 == "red":
            print("Burned by fire. Game Over.\n")
        elif choice2 == "blue":
            print("Eaten by beasts. Game Over.\n")
        elif choice2 == "yellow":
            print("You found the treasure. You win!\n")
        else:
            print("Game Over.\n")
    else:
        print("Attacked by crocodiles. Game Over.\n")
else:
    print("Fall into a hole. Game Over.\n")