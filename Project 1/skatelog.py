# A simple script to log skate sessions.
# It will create a log file with the date and time of the session, and the duration of the session.
# The log file will be saved in the same directory as the script.
# Usage: python skatelog.py
import json
import os
from datetime import datetime


# -----------------------------
# Utility Functions
# ------------------------------

def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return json.load(file)


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def initialize():
    os.makedirs("data", exist_ok=True)


# -----------------------------
# Menu
# -----------------------------

def main_menu():
    print("\n===== SkateLog =====")
    print("1. Add Session")
    print("2. View Sessions")
    print("3. Add Writing")
    print("4. View Writing")
    print("5. Add Media")
    print("6. View Media")
    print("7. View Stats")
    print("0. Exit")

    return input("Choose an option: ")


# -----------------------------
# Run Program
# -----------------------------

def run():
    initialize()

    sessions = load_data("data/sessions.json")
    writing = load_data("data/writing.json")
    media = load_data("data/media.json")

    while True:
        choice = main_menu()

        if choice == "0":
            print("Goodbye.")
            break
        else:
            print("Feature not implemented yet.")


if __name__ == "__main__":
    run()
