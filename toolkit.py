import random


# Stores tasks for the to-do list throughout the program's execution.
tasks = []


# TOOL 1: SIMPLE CALCULATOR
# Performs arithmetic operations on two numbers entered by the user.
def simple_calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("\nSelect an arithmetic operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1-4): ").strip()

        if operation == "1":
            result = first_number + second_number
        elif operation == "2":
            result = first_number - second_number
        elif operation == "3":
            result = first_number * second_number
        elif operation == "4":
            if second_number == 0:
                print("Error: Division by zero is not permitted.")
                return

            result = first_number / second_number
        else:
            print("Invalid operation. Please select an option from 1 to 4.")
            return

        print(f"\nCalculation result: {result:g}" if result.is_integer()
              else f"\nCalculation result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


# TOOL 2: TO-DO LIST MANAGER
# Enables users to add, view, and remove tasks from a mutable list.
def todo_list_manager():
    while True:
        print("\n--- TO-DO LIST MANAGER ---")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Return to the main menu")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            task = input("Enter the task description: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added successfully: {task}")
            else:
                print("The task description cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is currently empty.")
            else:
                print("\n--- YOUR TASKS ---")

                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks available to remove.")
                continue

            print("\n--- SELECT A TASK TO REMOVE ---")

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_number = int(
                    input("Enter the task number to remove: ")
                )

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task removed successfully: {removed_task}")
                else:
                    print("Invalid task number. Please try again.")

            except ValueError:
                print("Invalid input. Enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 4.")


# TOOL 3: NUMBER GUESSING GAME
# Generates a random number and guides the user until it is guessed correctly.
def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- NUMBER GUESSING GAME ---")
    print("I have selected a secret number between 1 and 10.")
    print("Try to guess the number!")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            if not 1 <= guess <= 10:
                print("Your guess must be between 1 and 10.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(
                    f"Congratulations! You guessed {secret_number} "
                    f"correctly in {attempts} attempt(s)."
                )
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")


# MAIN MENU
# Displays the available tools and continues until the user chooses to quit.
def main():
    print("=" * 44)
    print("WELCOME TO YOUR PERSONAL MINI-TOOLKIT")
    print("=" * 44)
    print("Explore simple tools built with Python.")

    while True:
        print("\n" + "=" * 44)
        print("             MAIN MENU")
        print("=" * 44)
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Number Guessing Game")
        print("4. Quit")
        print("=" * 44)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_list_manager()
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            print("\nThank you for using the Personal Mini-Toolkit!")
            print("Keep learning, keep coding, and have a great day!")
            break
        else:
            print(
                f"'{choice}' is not a valid option. "
                "Please enter a number between 1 and 4."
            )


# Execute the main function only when this file is run directly.
if __name__ == "__main__":
    main()
