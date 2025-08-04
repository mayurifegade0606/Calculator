import os
from colorama import init, Fore, Style
import pyfiglet

# Initialize colorama
init(autoreset=True)

history = []

# Calculator operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def modulus(x, y): return x % y
def power(x, y): return x ** y
def floor_div(x, y): return "Error! Division by zero." if y == 0 else x // y

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display menu
def show_menu():
    clear_screen()
    title = pyfiglet.figlet_format("CALCULATOR", font="slant")
    print(Fore.CYAN + title)
    print("╔═════════════════════════════════════╗")
    print("║ 1. Add (+)                          ║")
    print("║ 2. Subtract (-)                     ║")
    print("║ 3. Multiply (*)                     ║")
    print("║ 4. Divide (/)                       ║")
    print("║ 5. Modulus (%)                      ║")
    print("║ 6. Power (^)                        ║")
    print("║ 7. Floor Division (//)              ║")
    print("║ 8. Show History                     ║")
    print("║ 9. Clear Screen                     ║")
    print("║ 0. Exit                             ║")
    print("╚═════════════════════════════════════╝")

# Get numeric input safely
def get_number(prompt):
    while True:
        try:
            return float(input(Fore.YELLOW + prompt))
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input(Fore.MAGENTA + "Select an option (0-9): ")

    if choice == '0':
        confirm = input(Fore.YELLOW + "Are you sure you want to exit? (y/n): ").lower()
        if confirm == 'y':
            print(Fore.GREEN + "Exiting the calculator. Goodbye!")
            break
        else:
            continue

    elif choice == '8':
        if not history:
            print(Fore.LIGHTBLUE_EX + "\nNo calculations yet.")
        else:
            print(Fore.LIGHTCYAN_EX + f"\nCalculation History ({len(history)}):")
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")
        input(Fore.YELLOW + "\nPress Enter to continue...")
        continue

    elif choice == '9':
        clear_screen()
        continue

    elif choice in ['1','2','3','4','5','6','7']:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
            op = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            op = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            op = '*'
        elif choice == '4':
            result = divide(num1, num2)
            op = '/'
        elif choice == '5':
            result = modulus(num1, num2)
            op = '%'
        elif choice == '6':
            result = power(num1, num2)
            op = '^'
        elif choice == '7':
            result = floor_div(num1, num2)
            op = '//'

        history.append(f"{num1} {op} {num2} = {result}")
        print(Fore.GREEN + f"\nResult: {result}")
        input(Fore.YELLOW + "\nPress Enter to continue...")
    else:
        print(Fore.RED + "Invalid choice! Try again.")
        input(Fore.YELLOW + "\nPress Enter to continue...")
