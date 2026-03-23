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
