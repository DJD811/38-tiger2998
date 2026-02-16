
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

def add_session(sessions):
    print("\n--- Add Session---")

    spot = input("Enter spot name:")
    duration = input("Enter session duration")
    mood = input("Enter mood (1-5):")

    sessionw = {
        "spot": spot,
        "duration": duration, 
        "mood": mood,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    sessions.append(sessionw)
    save_data("data/sessions.json", sessions)
    print("Session saved successfully.")

def view_sessions(sessions):
    print("\n--- View Sessions ---")

    if not sessions:
        print("No sessions recorded yet.")
        return

    for index, session in enumerate(sessions, start=1):
        print(f"\nSession {index}")
        print("Spot:", session["spot"])
        print("Duration:", session["duration"])
        print("Mood:", session["mood"])
        print("Date:", session["date"])
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
        if choice == "1":
            add_session(sessions)
        elif choice == "2":
            view_sessions(sessions)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Feature not implemented yet.")


if __name__ == "__main__":
    run()
