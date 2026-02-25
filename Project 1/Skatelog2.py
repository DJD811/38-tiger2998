import json

print("Program Started")

data = []

user_choice = ""

while user_choice != "0":

    print("\nMain Menu")
    print("1 - Add Session")
    print("2 - View Sessions")
    print("3 - Add Writing")
    print("4 - View Writings")
    print("0 - Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        print("Add Session Selected")

    elif user_choice == "2":
        print("View Sessions Selected")

    elif user_choice == "3":
        print("Add Writing Selected")

    elif user_choice == "4":
        print("View Writings Selected")

    elif user_choice == "0":
        print("Exiting Program")

    else:
        print("Invalid Input")

print("Program Ended")