import random

def roll_die():
    return random.randint(1, 6)

def main():
    print("🎲 Welcome to the Die Rolling Game!")

    while True:
        # Step 2: Ask user to press 1
        user_input = input("Press 1 to roll the die: ")

        # Step 3: Check input
        if user_input != "1":
            print("❌ Error: You must press 1 to roll the die.")
            continue  # go back to step 2

        # Computer rolls die
        result = roll_die()
        print(f"🎲 You rolled: {result}")

        # Ask to play again
        play_again = input("Would you like to play again? (y/n): ").lower()

        if play_again != "y":
            print("Thanks for playing our game!")
            break  # End program

# Start program
if __name__ == "__main__":
    main()