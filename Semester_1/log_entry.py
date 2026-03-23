#Displays A Log Entry Message
print("Enter Log Entry")
def add_entry(writing):
    print("\n--- Add Entry ---")

    title = input("Enter title: ")
    content = input("Enter your reflection: ")

    word_count = len(content.split())

    entry = {
        "title": title,
        "content": content,
        "word_count": word_count,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    writing.append(entry)
    save_data("data/writing.json", writing)

    print("Entry saved successfully.")