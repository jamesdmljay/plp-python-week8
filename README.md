README.md# Personal Mini-Toolkit

## Project Description

The Personal Mini-Toolkit is a menu-driven Python program that combines three useful tools in one application. It was developed as the final project for the PLP Python course.

## Features

1. **Simple Calculator:** Adds, subtracts, multiplies, and divides two numbers.
2. **To-Do List Manager:** Adds, displays, and removes tasks using a Python list.
3. **Number Guessing Game:** Challenges the user to guess a randomly selected number between 1 and 10.

The program includes a repeating menu, input validation, conditional statements, loops, lists, functions, comments, exception handling, and f-strings.

## Requirements

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code or a terminal.

## How to Run

1. Clone or download this repository.
2. Open the project folder in your code editor or terminal.
3. Run the following command:

```bash
python toolkit.py
```

On some Windows computers, use:

```bash
py toolkit.py
```

4. Choose an option from the menu and follow the instructions.
5. Select option 4 to exit the program.

## Project Structure

- `toolkit_plan.txt` — the project blueprint.
- `toolkit.py` — the complete Python application.
- `screenshots/` — screenshots showing the menu, invalid input handling, and each tool in action.
- `README.md` — project documentation and reflection.

## Reflection

The most challenging part of this project was designing a menu that returns after each tool finishes without restarting the entire program. The bug that took the longest to fix was handling invalid user input without allowing the program to crash. I addressed this by using conditional statements and exception handling. Building the to-do list helped me understand how Python lists can store changing information during program execution. The guessing game improved my understanding of loops and decision-making. I also learned the importance of writing readable code with comments and meaningful messages. If I had one more week, I would add a feature that saves tasks to a file so that they remain available after the program closes.
