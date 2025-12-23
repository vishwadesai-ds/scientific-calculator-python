# 🧮 Scientific Calculator (Python CLI)

A **menu-driven scientific calculator** built using **Python**, implemented in **two versions** to demonstrate progressive learning:

1. **Procedural Programming (Python fundamentals)**
2. **Object-Oriented Programming (OOP) refactor**

This project is designed to showcase **core Python skills required for Data Science and Software roles**.

---

## 📁 Project Structure

scientific_calculator/
|
|-- calculator.py          # Procedural implementation (Python basics)
|-- calculator_oops.py     # Object-Oriented implementation (OOP)
|-- README.md

---

## 🎯 Project Objectives

- Build a complete CLI-based calculator from scratch
- Practice Python fundamentals (loops, functions, conditionals)
- Implement scientific computations using the math module
- Handle user input safely with error handling
- Store and display calculation history
- Refactor procedural code into a clean OOP design

---

## ✨ Features

### 🔹 Basic Operations
- Addition (supports variable number of inputs)
- Subtraction
- Multiplication (supports variable number of inputs)
- Division (with zero-division handling)
- Modulus
- Power

### 🔹 Scientific Operations
- Square Root
- Power
- Natural Logarithm (ln)
- Logarithm Base 10
- Trigonometric Functions: sin, cos, tan (radians)
- Factorial
- Absolute Value
- Exponential (e^x)

### 🔹 Expression Evaluation
- Evaluate full mathematical expressions such as:
  2 + 3 * sqrt(4) + sin(0)
- Uses safe evaluation with restricted built-ins
- Supports math functions and constants (pi, e)
- Prevents unsafe operations (import, open, etc.)

### 🔹 History Management
- Stores all successful calculations
- Displays numbered calculation history
- Session-based (clears on restart)

### 🔹 User Experience
- Clear, structured menus
- Input validation (safe_int, safe_float)
- Clean CLI output
- Friendly error messages

---

## 🧠 Concepts Covered

### Python Fundamentals
- Variables and Data Types
- Functions
- Loops
- Conditional statements
- Exception handling (try-except)
- String manipulation
- Lists

### Python Libraries
- math module
- Built-in functions (abs, round)

### Object-Oriented Programming (OOP)
- Classes and Objects
- Constructor (__init__)
- Encapsulation
- Method organization
- Single Responsibility Principle
- Clean separation of logic and UI

### Security and Best Practices
- Restricted use of eval
- Whitelisting allowed functions
- Blocking dangerous keywords
- Defensive input handling

---

## ▶️ How to Run

### Prerequisites
- Python 3.x
- No external libraries required

### Run Procedural Version
python calculator.py

### Run OOP Version
python calculator_oops.py

### Example Run
Enter choice: 3  
Enter expression: 23 + 23 - 3 / 2 * 2 + sin(0) + cos(0)  
Result: 44  

---

## 📌 Why Two Versions?

This project intentionally includes two implementations to demonstrate learning progression.

calculator.py
- Demonstrates Python fundamentals
- Suitable for beginners
- Focuses on logic and control flow

calculator_oops.py
- Refactors the same logic using OOP
- Demonstrates class-based design
- Shows progression from basics to structured code

---

## 🚀 Future Improvements

- Degree to Radian mode toggle
- Persistent history using file storage
- Unit testing
- GUI version (Tkinter or Streamlit)
- Packaging as a Python module

---

## 👤 Author

Vishwa Desai  
Data Science Student  
Building strong foundations in Python, SQL, and Machine Learning.

---

## ⭐ Final Note

This project is part of a learning-focused portfolio, emphasizing:
- clarity over complexity
- correctness over shortcuts
- fundamentals before frameworks

Feedback and suggestions are welcome.