"""
Scientific Calculator (Python CLI)

Author: Vishwa Desai
GitHub: https://github.com/vishwadesai.ds
License: MIT
"""

import math

print("... Welcome to a calculating life ...")

def clear_screen():
    print("\n" * 50)

MAIN_MENU = """
════════════════════════════════════
   🧮 SCIENTIFIC CALCULATOR
════════════════════════════════════
1. Basic Operations
2. Scientific Operations
3. Evaluate Expression
4. View History
5. Exit
════════════════════════════════════
"""

BASIC_MENU = """
--- BASIC OPERATIONS ---
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
0. Back to Main Menu
"""

SCIENTIFIC_MENU = """
--- SCIENTIFIC OPERATIONS ---
1. Square Root (√x)
2. Power (xʸ)
3. Natural Logarithm (ln x)
4. Logarithm Base 10 (log₁₀ x)
5. Sine (sin x)
6. Cosine (cos x)
7. Tangent (tan x)
8. Factorial (x!)
9. Absolute Value (|x|)
10. Exponential (eˣ)
0. Back to Main Menu
Note: Trigonometric functions use radians
"""

def safe_int(prompt=""):
    try:
        return int(input(prompt))
    except ValueError:
        print("❌ Please enter a valid integer")
        return None

def safe_float(prompt=""):
    try:
        return float(input(prompt))
    except ValueError:
        print("❌ Please enter a valid number")
        return None

def addition(nums):
    return sum(float(i) for i in nums)

def multiplication(nums):
    result = 1.0
    for i in nums:
        result *= float(i)
    return result

def subtraction(a, b):
    return float(a) - float(b)

def division(a, b):
    return float(a) / float(b)

def modulus(a, b):
    return float(a) % float(b)

def power(a, b):
    return float(a) ** float(b)

history = []
next_iteration = True

while next_iteration:
    clear_screen()
    print(MAIN_MENU)

    operate = safe_int("Enter choice: ")
    if operate is None:
        continue

    # ---------------- BASIC ----------------
    if operate == 1:
        while True:
            clear_screen()
            print(BASIC_MENU)

            basic = safe_int("Enter choice: ")
            if basic is None:
                continue

            if basic == 1:
                nums = input("Enter numbers separated by space: ").split()
                result = round(addition(nums), 6)
                history.append(f"{' + '.join(nums)} = {result}")
                print("Result:", result)

            elif basic == 2:
                nums = input("Enter two numbers: ").split()
                try:
                    result = round(subtraction(nums[0], nums[1]), 6)
                    history.append(f"{nums[0]} - {nums[1]} = {result}")
                    print("Result:", result)
                except:
                    print("❌ Invalid input")

            elif basic == 3:
                nums = input("Enter numbers separated by space: ").split()
                result = round(multiplication(nums), 6)
                history.append(f"{' * '.join(nums)} = {result}")
                print("Result:", result)

            elif basic == 4:
                nums = input("Enter two numbers: ").split()
                try:
                    a, b = float(nums[0]), float(nums[1])
                    if b == 0:
                        print("❌ Division by zero")
                        continue
                    result = round(division(a, b), 6)
                    history.append(f"{a} / {b} = {result}")
                    print("Result:", result)
                except:
                    print("❌ Invalid input")

            elif basic == 5:
                nums = input("Enter two numbers: ").split()
                try:
                    a, b = float(nums[0]), float(nums[1])
                    if b == 0:
                        print("❌ Modulus by zero")
                        continue
                    result = round(modulus(a, b), 6)
                    history.append(f"{a} % {b} = {result}")
                    print("Result:", result)
                except:
                    print("❌ Invalid input")

            elif basic == 6:
                nums = input("Enter base and power: ").split()
                try:
                    result = round(power(nums[0], nums[1]), 6)
                    history.append(f"{nums[0]} ** {nums[1]} = {result}")
                    print("Result:", result)
                except:
                    print("❌ Invalid input")

            elif basic == 0:
                break

    # ---------------- SCIENTIFIC ----------------
    elif operate == 2:
        while True:
            clear_screen()
            print(SCIENTIFIC_MENU)

            sci = safe_int("Enter choice: ")
            if sci is None:
                continue

            if sci == 1:
                x = safe_float("Enter x: ")
                if x is None or x < 0:
                    print("❌ Invalid input")
                    continue
                result = round(math.sqrt(x), 6)
                history.append(f"sqrt({x}) = {result}")
                print("Result:", result)

            elif sci == 2:
                nums = input("Enter base and power: ").split()
                try:
                    result = round(math.pow(float(nums[0]), float(nums[1])), 6)
                    history.append(f"{nums[0]} ^ {nums[1]} = {result}")
                    print("Result:", result)
                except:
                    print("❌ Invalid input")

            elif sci == 3:
                x = safe_float("Enter x (>0): ")
                if x is None or x <= 0:
                    print("❌ Invalid input")
                    continue
                result = round(math.log(x), 6)
                history.append(f"log({x}) = {result}")
                print("Result:", result)

            elif sci == 4:
                x = safe_float("Enter x (>0): ")
                if x is None or x <= 0:
                    print("❌ Invalid input")
                    continue
                result = round(math.log10(x), 6)
                history.append(f"log10({x}) = {result}")
                print("Result:", result)

            elif sci == 5:
                x = safe_float("Enter x: ")
                if x is None:
                    continue
                result = round(math.sin(x), 6)
                history.append(f"sin({x}) = {result}")
                print("Result:", result)

            elif sci == 6:
                x = safe_float("Enter x: ")
                if x is None:
                    continue
                result = round(math.cos(x), 6)
                history.append(f"cos({x}) = {result}")
                print("Result:", result)

            elif sci == 7:
                x = safe_float("Enter x: ")
                if x is None:
                    continue
                result = round(math.tan(x), 6)
                history.append(f"tan({x}) = {result}")
                print("Result:", result)

            elif sci == 8:
                x = safe_int("Enter integer x (≥0): ")
                if x is None or x < 0:
                    print("❌ Invalid input")
                    continue
                result = math.factorial(x)
                history.append(f"factorial({x}) = {result}")
                print("Result:", result)

            elif sci == 9:
                x = safe_float("Enter x: ")
                if x is None:
                    continue
                result = round(abs(x), 6)
                history.append(f"abs({x}) = {result}")
                print("Result:", result)

            elif sci == 10:
                x = safe_float("Enter x: ")
                if x is None:
                    continue
                result = round(math.exp(x), 6)
                history.append(f"e^{x} = {result}")
                print("Result:", result)

            elif sci == 0:
                break

    # ---------------- EXPRESSION ----------------
    elif operate == 3:
        expression = input("Enter expression: ")

        forbidden = ["import", "__", "os", "sys", "open", "eval", "exec"]
        if any(word in expression for word in forbidden):
            print("❌ Invalid expression")
        else:
            try:
                allowed = {
                    "sin": math.sin,
                    "cos": math.cos,
                    "tan": math.tan,
                    "log": math.log,
                    "log10": math.log10,
                    "sqrt": math.sqrt,
                    "abs": abs,
                    "pi": math.pi,
                    "e": math.e
                }
                result = round(eval(expression, {"__builtins__": None}, allowed), 6)
                history.append(f"{expression} = {result}")
                print("Result:", result)
            except:
                print("❌ Invalid expression")

    # ---------------- HISTORY ----------------
    elif operate == 4:
        clear_screen()
        if not history:
            print("📭 No history yet")
        else:
            print("--- Calculation History ---")
            for i, item in enumerate(history, 1):
                print(f"{i}. {item}")
        input("\nPress Enter to continue...")

    elif operate == 5:
        next_iteration = False

print("... See you soon again ...")