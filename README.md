# pr7_modularandpackager
# moduler-and-packager
# 🧰 Multi-Utility Toolkit (Moduler & Packager)

## 📌 Project Overview
The **Multi-Utility Toolkit** is a Python-based console application that integrates multiple **standard modules**, **custom modules**, and **packages** to perform a variety of tasks. It demonstrates the effective use of Python's modular structure and provides utility functions for **date-time operations**, **mathematical computations**, **random data generation**, and **unique identifier creation**.

This project is built to demonstrate core Python concepts including **built-in modules (`datetime`, `time`, `math`, `random`, `uuid`)**, **custom modules**, **packages with `__init__.py`**, **`__name__` and `__main__`**, and the **`dir()`** function.

---

## 🎯 Objectives
- **Explore Built-in Modules:** Utilize `datetime`, `time`, `math`, `random`, and `uuid` modules for practical tasks
- **Custom Modules and Packages:**
  - Create modular Python scripts for specific functionalities
  - Organize them into packages with an `__init__.py` file to demonstrate package usage
- **Script Organization:** Implement `__name__` and `__main__` to separate reusable components and main execution logic
- **Dynamic Exploration:** Use the `dir()` function to explore module attributes dynamically

---

## 🛠️ Features

### ⏰ Datetime and Time Module
- Display current date and time in a user-friendly format
- Calculate the difference between two dates or times
- Format dates into custom formats using `strftime`
- Simple stopwatch and countdown timer

### ➗ Math Module
- Arithmetic and advanced operations such as trigonometry, factorials, and logarithms
- Real-world problem solving: compound interest and area of geometric shapes

### 🎲 Random Module
- Generate random numbers, lists, and passwords
- Generate a random OTP

### 🆔 UUID Module
- Generate unique identifiers (e.g., for invoices)

### 📁 File Operations (Custom Module)
- Create, write, read, and append text files
- Save all logs and outputs into text files via a custom module

### 🔍 Module Exploration
- Dynamically explore the attributes of any module using `dir()`

---

## 💼 Example Use Case
A small business owner uses the toolkit to manage their daily operations. They:
- Calculate working hours using the `time` module
- Generate random passwords for their team
- Assign unique identifiers to invoices using the `uuid` module
- Save all logs and outputs into text files via a custom module
- Dynamically explore the capabilities of the toolkit using `dir()`

---

## 🧠 Concepts Used

### ✅ Built-in (Standard) Modules
- `datetime` – current date/time, date differences, `strftime` formatting
- `time` – stopwatch, countdown timer, working-hours calculation
- `math` – factorial, trigonometry, logarithms, `pi`, `pow`
- `random` – random numbers, lists, passwords, OTPs
- `uuid` – unique identifier generation

### ✅ Custom Modules and Packages
- Separate `.py` files for each functionality
- A package folder containing an `__init__.py` file
- Importing custom modules into the main program

### ✅ Script Organization
- `if __name__ == "__main__":` to keep reusable functions separate from main execution logic

### ✅ Dynamic Exploration
- `dir()` to list the attributes and functions of any module

---

## 🧾 Program Structure

```
Moduler_and_Packager/
│
├── main.py                     # Main program (menu + execution logic)
├── toolkit/                    # Package
│   ├── __init__.py             # Package initializer
│   ├── datetime_ops.py         # Datetime and time operations
│   ├── math_ops.py             # Mathematical operations
│   ├── random_ops.py           # Random data generation
│   ├── uuid_ops.py             # UUID generation
│   ├── file_ops.py             # File operations (custom module)
│   └── explorer.py             # dir() based module exploration
└── README.md                   # Project documentation
```

---

## ▶️ How to Run the Program
1. Install **Python 3.x** on your system
2. Clone the repository:
   ```
   git clone <your-repository-url>
   ```
3. Open terminal / command prompt
4. Navigate to the project folder
5. Run the command:

```
python main.py
```

---

## 🖥️ Sample Console Interaction

### Main Menu
```
============================
Welcome to Multi-Utility Toolkit
============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
============================
Enter your choice: 1
```

### Datetime and Time Operations
```
Datetime and Time Operations:
1. Display current date and time
2. Calculate difference between two dates/times
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
Enter your choice: 1

Current Date and Time: 2025-01-04 10:15:30
============================
Enter your choice: 2

Enter the first date (YYYY-MM-DD): 2024-12-25
Enter the second date (YYYY-MM-DD): 2025-01-04
Difference: 10 days
============================
Enter your choice: 6
```

### Mathematical Operations
```
Mathematical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Menu
Enter your choice: 1

Enter a number: 5
Factorial: 120
============================
Enter your choice: 2

Enter principal amount: 1000
Enter rate of interest (in %): 5
Enter time (in years): 2
Compound Interest: 1102.50
============================
Enter your choice: 5
```

### Random Data Generation
```
Random Data Generation:
1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Back to Main Menu
Enter your choice: 3

Enter password length: 8
Generated Password: Kd8@qzP!
============================
Enter your choice: 5
```

### Generate Unique Identifiers (UUID)
```
Generate Unique Identifiers:

Generated UUID: f47ac10b-58cc-4372-a567-0e02b2c3d479
============================
Enter your choice: 3
```

### File Operations (Custom Module)
```
File Operations:
1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
5. Back to Main Menu
Enter your choice: 1

Enter file name: example.txt
File created successfully!
============================
Enter your choice: 2

Enter file name: example.txt
Enter data to write: This is a sample file.
Data written successfully!
============================
Enter your choice: 3

Enter file name: example.txt
File Content:
This is a sample file.
============================
Enter your choice: 5
```

### Explore Module Attributes (dir())
```
Explore Module Attributes:
Enter module name to explore: math
Available Attributes in math module:
['acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'ceil', 'comb',
'copysign', 'cos', ...]
============================
```

### Exit
```
============================
Thank you for using the Multi-Utility Toolkit!
============================
```

---

## 🔐 Program Flow
1. **Welcome and Main Menu** – Display the welcome banner and the list of 7 options
2. **User Choice** – The user selects an option (1–7); each option opens its own sub-menu
3. **Sub-Menu Operations** – The relevant custom module from the package performs the task (datetime, math, random, UUID, file, or `dir()` exploration)
4. **Return to Menu** – Each sub-menu has a "Back to Main Menu" option; the main menu repeats until the user exits
5. **Exit Message** – Option 7 ends the program with a thank-you message

---

## 📝 Assumptions
- Dates are entered in the format **`YYYY-MM-DD`**
- The **compound interest** output follows the sample (1000, 5%, 2 years → `1102.50`), i.e. it displays the **final amount** (`P × (1 + R/100)^T`), formatted to 2 decimal places
- Trigonometric calculations accept the angle in **degrees**, which is converted to radians using `math.radians()`
- Area of geometric shapes supports **circle, rectangle, triangle, and square**
- Random number generation uses a **user-defined range**; random list uses a user-defined size and range
- Passwords contain **letters, digits, and special characters** (`string` module); the OTP is a **6-digit numeric code**
- Stopwatch starts and stops on **Enter key press**; countdown timer takes the duration **in seconds**
- File operations work on files in the **current working directory**; logs and outputs are saved as **`.txt`** files
- Invalid menu choices and invalid inputs display an **error message** and prompt again
- The module explorer accepts the **name of any importable module**; if the module is not found, an error message is shown

---

## 🚀 Future Enhancements
- Save logs to CSV / JSON formats
- Stronger input validation
- GUI version using **Tkinter** or **PyQt**
- Invoice management using UUIDs and file storage

---

## 👨‍💻 Author
Python Developer | apeksha

---

## 📄 License
This project is created for **educational purposes** and is free to use and modify.

---

✨ *Happy Coding!* ✨
