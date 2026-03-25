# Python Project Portfolio

This repository contains a collection of Python projects developed to demonstrate various programming concepts, problem-solving skills, and application development. Each project is designed to showcase different aspects of Python's capabilities, from simple interactive games to data management applications.

---

## SkateLog Application

SkateLog is a command-line application designed to help skateboarders track and manage their skating sessions. It allows users to log details about each session, such as the spot, duration, and mood, and stores this information persistently using JSON files. This project serves as a practical example of data persistence, menu-driven interaction, and basic data management in Python.

### Features

-   **Session Logging**: Record details for each skate session including spot name, duration, mood (1-5), and the date.
-   **View Sessions**: Display a list of all recorded skate sessions with their details.
-   **Data Persistence**: Sessions are saved to and loaded from a JSON file (`data/sessions.json`), ensuring data is not lost between application runs.
-   **Menu-Driven Interface**: Easy navigation through a main menu to choose different actions.
-   **Directory Management**: Automatically creates a `data` directory if it doesn't exist to store JSON files.
-   **Modular Design**: Functions are organized into logical units for better readability and maintainability.

### Technologies Used

-   **Python 3**: The primary programming language.
-   **`json` module**: Used for serializing and deserializing Python objects (lists of dictionaries) to and from JSON files, enabling data persistence.
-   **`os` module**: Utilized for operating system interactions, specifically to check for and create directories (`os.path.exists`, `os.makedirs`).
-   **`datetime` module**: Employed to capture the current date for each logged session, formatting it as `YYYY-MM-DD`.
-   **Standard I/O**: `input()` for user commands and `print()` for displaying information and menus.

### How It Works

1.  **Initialization**: Upon starting, the `run()` function calls `initialize()` to ensure a `data` directory exists. It then loads existing session data, writing data, and media data from `data/sessions.json`, `data/writing.json`, and `data/media.json` respectively. If files don't exist, it starts with empty lists.
2.  **Main Menu Loop**: The application enters a loop, continuously displaying the `main_menu()` with options to add/view sessions, writing, media, view stats, or exit.
3.  **User Choice Handling**: Based on the user's input:
    -   **Add Session (`1`)**: Prompts for spot, duration, and mood. It then creates a dictionary with these details plus the current date, appends it to the `sessions` list, and saves the updated list to `data/sessions.json`.
    -   **View Sessions (`2`)**: Checks if any sessions are recorded. If so, it iterates through the `sessions` list and prints each session's details in a readable format.
    -   **Exit (`0`)**: Terminates the application gracefully.
    -   **Other Options (`3` to `7`)**: Currently display a "Feature not implemented yet." message.
4.  **Data Management**: The `load_data()` and `save_data()` functions abstract away the file handling, making it easy to read from and write to JSON files.

### What I Learned

Developing the SkateLog application was an excellent opportunity to solidify my understanding of several core Python concepts:

-   **File I/O and JSON Persistence**: I gained hands-on experience with reading from and writing to files using `json.load()` and `json.dump()`. This taught me how to store and retrieve application data, making it persistent across different runs.
-   **Modular Programming with Functions**: Organizing the code into distinct functions (`load_data`, `save_data`, `add_session`, `view_sessions`, `main_menu`, `initialize`, `run`) improved code readability, reusability, and made the application easier to manage.
-   **Handling Dates and Times**: Using the `datetime` module, specifically `datetime.now().strftime()`, was crucial for automatically timestamping each skate session, a common requirement in data logging applications.
-   **Basic Error Handling (File/Directory Existence)**: The `initialize()` function and `os.path.exists()` demonstrated how to gracefully handle the absence of a data directory or data files, preventing errors and ensuring a smooth user experience.
-   **List and Dictionary Manipulation**: The application heavily relies on appending dictionaries to a list and accessing dictionary values, reinforcing fundamental data structure operations in Python.
-   **User Interface Design (CLI)**: Designing a simple, intuitive text-based menu and handling user input through `input()` functions provided practical experience in command-line interface development.
-   **Program Flow Control**: The `while True` loop and `if/elif/else` statements in the `run()` function helped me understand how to control the application's flow based on user choices.

### Challenges Faced

Throughout this project, I encountered a few challenges that pushed my learning:

-   **Data Serialization/Deserialization**: Understanding how Python objects (lists of dictionaries) are converted to JSON strings for storage and back again for use was initially a bit tricky. I had to ensure the `json.dump` and `json.load` operations were handled correctly.
-   **Managing File Paths and Directories**: Ensuring the `data` directory was created and that the JSON files were accessed from the correct path required careful use of the `os` module. Debugging file not found errors taught me the importance of robust path handling.
-   **Handling Incomplete Features**: Deciding how to gracefully inform the user about unimplemented features (like "Add Media" or "View Stats") without crashing the program was an important design consideration. I chose to provide a clear message indicating these features are still under development.
-   **Input Validation (Future Consideration)**: While not fully implemented for all inputs (e.g., mood validation), I recognized the need for more robust input validation to prevent invalid data from being stored, which is a key learning point for future improvements.

### Future Improvements

SkateLog has a solid foundation and can be expanded with many exciting features:

-   **Comprehensive Input Validation**: Implement stricter validation for all user inputs (e.g., ensuring mood is within 1-5, duration is a number).
-   **Data Editing and Deletion**: Allow users to modify existing session entries or delete them.
-   **Advanced Statistics**: Develop the "View Stats" feature to calculate and display more insightful metrics (e.g., average session duration, most visited spot, mood trends).
-   **Search and Filter Sessions**: Add functionality to search for sessions by spot, date range, or mood.
-   **Add Writing/Media Functionality**: Implement the remaining menu options to add and view writing entries and media links.
-   **User Accounts**: Introduce a basic user authentication system to manage multiple users' skate logs.
-   **Command-Line Arguments**: Allow some operations to be performed directly via command-line arguments.
-   **Graphical User Interface (GUI)**: Transition from a text-based interface to a more user-friendly graphical interface using libraries like Tkinter, PyQt, or Kivy.

### How to Run the Project

To run the SkateLog application on your local machine, follow these steps:

1.  **Save the Code**: Save the provided Python code into a file named `skatelog.py`.
2.  **Open Terminal**: Open your preferred terminal or command prompt.
3.  **Navigate to Directory**: Use the `cd` command to navigate to the directory where you saved `skatelog.py`.
    ```bash
    cd path/to/your/Python\ Project\ directory
    ```
4.  **Run the Application**: Execute the Python script using the following command:
    ```bash
    python skatelog.py
    ```
5.  **Interact**: Follow the on-screen menu to add or view your skate sessions!

---

## Dice Rolling Game

A simple and interactive command-line application that simulates the rolling of a six-sided die. This project provides a foundational example of user interaction, random number generation, and basic game loop implementation in Python.

### Features

-   **Simulated Die Roll**: Accurately simulates the roll of a standard six-sided die (values 1-6).
-   **Interactive User Input**: Prompts the user to initiate each die roll.
-   **Immediate Feedback**: Displays the result of each roll directly to the console.
-   **Play Again Option**: Allows users to continue rolling the die for multiple rounds.
-   **Basic Input Validation**: Ensures the user provides valid input to roll the die.

### Technologies Used

-   **Python 3**: The core programming language used for the application logic.
-   **`random` module**: Utilized for generating pseudo-random integers to simulate the die roll.
-   **Standard I/O**: Employs `input()` for user interaction and `print()` for displaying game messages and results.

### How It Works

The game operates through a continuous loop within the `main()` function:

1.  **Welcome Message**: The game starts with a friendly welcome message.
2.  **User Prompt**: It repeatedly asks the user to type `1` to roll the die.
3.  **Input Validation**: If the user enters anything other than `1`, an error message is displayed, and the prompt is repeated.
4.  **Die Roll**: Upon valid input, the `roll_die()` function is called, which returns a random integer between 1 and 6.
5.  **Display Result**: The rolled number is then printed to the console.
6.  **Play Again**: The user is asked if they wish to roll again. Entering `y` (or `Y`) continues the loop, while any other input terminates the game.

### What I Learned

Developing this project provided valuable hands-on experience with several fundamental Python concepts:

-   **Leveraging the `random` module**: Understanding how to import and use modules, specifically `random.randint()` for generating unpredictable outcomes.
-   **Defining and Calling Functions**: Practicing with function definitions (`roll_die()`, `main()`) to encapsulate specific pieces of logic, making the code more organized and reusable.
-   **Implementing `while` Loops**: Mastering `while True` loops for creating persistent game sessions and managing program flow based on user decisions.
-   **Conditional Logic (`if`/`else`)**: Gaining proficiency in using `if` and `else` statements for decision-making, such as validating user input and determining whether to continue or end the game.
-   **Handling User Input**: Working with the `input()` function to receive text-based commands from the user and processing them effectively.
-   **Formatted Output (f-strings)**: Using f-strings to embed variables directly within print statements for clear and readable output.
-   **Basic Flow Control (`continue`, `break`)**: Understanding how `continue` can restart a loop iteration and `break` can exit a loop entirely, crucial for interactive applications.
-   **Python Script Entry Point (`if __name__ == "__main__"`)**: Learning the conventional way to define the starting point of a Python script.

### Challenges Faced

As a student developer, I encountered and overcame a few common challenges during this project:

-   **Ensuring Valid User Input**: Initially, handling unexpected input (e.g., pressing a letter instead of `1`) required careful thought to prevent crashes and provide helpful feedback. I learned the importance of robust input validation.
-   **Managing the Game Flow**: Structuring the `while` loop and its exit conditions (`play_again`) to ensure the game continued smoothly or ended gracefully was a key learning curve.
-   **Debugging Logic Errors**: Identifying why the game might not behave as expected (e.g., incorrect `break` or `continue` placement) reinforced my debugging skills.

### Future Improvements

This simple game can be expanded in many exciting ways:

-   **Multiple Dice**: Allow the user to specify the number of dice to roll simultaneously.
-   **Customizable Dice**: Implement support for dice with different numbers of sides (e.g., d4, d8, d12, d20).
-   **Score Tracking**: Add functionality to keep a running score or track statistics of rolls.
-   **Graphical User Interface (GUI)**: Migrate from a command-line interface to a more visually appealing GUI using libraries like Tkinter, PyQt, or Kivy.
-   **Two-Player Mode**: Introduce a second player and define rules for competition.
-   **Betting System**: Incorporate a simple betting mechanism to make the game more engaging.

### How to Run the Project

To get this dice rolling game up and running on your local machine, follow these steps:

1.  **Save the Code**: Save the provided Python code into a file named `dice_game.py`.
2.  **Open Terminal**: Open your preferred terminal or command prompt.
3.  **Navigate to Directory**: Use the `cd` command to navigate to the directory where you saved `dice_game.py`.
    ```bash
    cd path/to/your/Python\ Project\ directory
    ```
4.  **Run the Game**: Execute the Python script using the following command:
    ```bash
    python dice_game.py
    ```
5.  **Play**: Follow the on-screen prompts to roll the die and play the game!
