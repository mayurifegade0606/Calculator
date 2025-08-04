
# CLI Calculator App

This is a simple and interactive **Command-Line Calculator** built in Python.  
It supports basic arithmetic operations and has a clean, colored interface designed for the terminal.

---

## 🚀 Features

- Basic operations: Add, Subtract, Multiply, Divide  
- Advanced operations: Modulus, Power, Floor Division  
- Input validation to prevent crashes  
- Operation history tracking  
- Screen clearing feature  
- Styled CLI UI using `colorama` and `pyfiglet`

---

## 🛠️ How to Run

1. Clone or download this repository to your system.
2. Open a terminal and navigate to the project directory:
   ```bash
   cd CalculatorApp
   ```
3. Install dependencies (only required once):
   ```bash
   pip install colorama pyfiglet
   ```
4. Run the calculator:
   ```bash
   python calculator.py
   ```

---

## 💻 Sample Output

```
    _________    __    ________  ____    ___  __________  ____  
   / ____/   |  / /   / ____/ / / / /   /   |/_  __/ __ \/ __ \ 
  / /   / /| | / /   / /   / / / / /   / /| | / / / / / / /_/ / 
 / /___/ ___ |/ /___/ /___/ /_/ / /___/ ___ |/ / / /_/ / _, _/  
 \____/_/  |_/_____/\____/\____/_____/_/  |_/_/  \____/_/ |_|   

╔═════════════════════════════════════╗
║ 1. Add (+)                          ║
║ 2. Subtract (-)                     ║
║ 3. Multiply (*)                     ║
║ 4. Divide (/)                       ║
║ 5. Modulus (%)                      ║
║ 6. Power (^)                        ║
║ 7. Floor Division (//)              ║
║ 8. Show History                     ║
║ 9. Clear Screen                     ║
║ 0. Exit                             ║
╚═════════════════════════════════════╝

Select an option (0-9): 3  
Enter first number: 5  
Enter second number: 6  

Result: 30.0  

Press Enter to continue...  
Select an option (0-9): 5  
Enter first number: 10  
Enter second number: 5  

Result: 0.0  

Press Enter to continue...  
Calculation History (2):  
1. 5.0 * 6.0 = 30.0  
2. 10.0 % 5.0 = 0.0  
Select an option (0-9): 0  
Are you sure you want to exit? (y/n): y  
Exiting the calculator. Goodbye!
```

---

## 📁 Project Structure

```
CalculatorApp/
├── calculator.py
└── README.md
```

---

## ✍️ Author

Created by **Mayuri Fegade**  

