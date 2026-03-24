import random
# Print Welcome Message!
print("Welcome to the Sailor Dice Game! Pick your Occupation! 🎲")
userRollResponseString = input("Press 1 to roll the die: ")

# Step 3: Validate input
while userRollResponseString != "1":
    print("Error! You must press 1 to roll the die.")
dice_roll = random.randint(1, 6)

print(f"The die rolled: {dice_roll}")

if dice_roll ==1:
    print("You rolled a 1! You are a fisherman! You will have a simple quite life, but will never go hungry.")        
if dice_roll ==2:
    print("You rolled a 2! You are a shipwright! Your hands are skilled at building, You will always have work,")
if dice_roll ==3:
    print("You rolled a 3! You are a navigator! Your sense of direction is unparalleled, and you will always find your way.")
if dice_roll ==4:
    print("You rolled a 4! You are a cook! Your culinary skills will keep your crew happy and well-fed.")
if dice_roll ==5:
    print("You rolled a 5! You are a merchant! Your business acumen will lead you to great wealth.")
if dice_roll ==6:
    print("You rolled a 6! You are a captain! Your leadership will guide your crew to victory.")

    play_again = input("Do you want to play again? Please type yes or no:").lower()

    # Step 8: Decision
    if play_again == "yes":
        userRollResponseString = input("Press 1 to roll the die: ")
    else:
        print("Thank you for playing this Sailor Dice Game. Safe travels Sinbad!")
     # End the program
