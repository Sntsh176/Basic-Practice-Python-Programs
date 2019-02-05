"""
This is the random guess game
Here Player wil have to enter number 0-9
Computer will match the number using random
"""


import random
counter = 0

while True:
    print ("Hey want to play , press ENTER or write 'exit'")
    choice = input("\nPlease enter your choice : ")
    
    if choice.lower() == "exit":
        print("\nExiting from the Game ... byeeee...")
        break
    number = int(input("Please enter a Number 1-9 : "))
    counter += 1
    rad_number = random.randint(1,9)
    if number == rad_number:
        print("Your guess is exactly right ")
    elif number > rad_number:
        print("Your guess is too high ")
    else:
        print("Your guess is too low ")

print("Total attempt for the Game play was : ", counter)