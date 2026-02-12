import random
print("Welcome to the Sailor Dice Game! Pick your Occupation! 🎲")
while True:
    user_input = input("Press 1 to roll the die:")

    # Step 3: Validate input
    if user_input != "1":
        print("Error! You must press 1 to roll the die.")
        continue 
    dice_roll = random.randint(1, 6)

    print(f"The die rolled: {dice_roll}")
    play_again = input("Do you want to play again? Please type yes or no:").lower()

    # Step 8: Decision
    if play_again == "yes":
        continue
    else:
        print("Thank you for playing this Sailor Dice Game. Safe travels Sinbad!")
        break  # End the program
