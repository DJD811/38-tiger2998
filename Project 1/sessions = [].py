def add_session(sessions):
    print("\n--- Add Session ---")

    spot = input("Enter spot name: ")
    duration = input("Enter duration (minutes): ")
    mood = input("Enter mood (1-5): ")

    session = {
        "spot": spot,
        "duration": duration,
        "mood": mood,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    sessions.append(session)
    save_data("data/sessions.json", sessions)

    print("Session saved successfully.")
