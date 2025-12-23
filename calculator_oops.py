"""
Scientific Calculator using OOPS (Python CLI)

Author: Vishwa Desai
GitHub: https://github.com/vishwadesai.ds
License: MIT
"""

import math

class ScientificCalculator:
    """
    Main Calculator Class

    This class encapsulates:
    - Calculator state (history)
    - All calculation logic
    - Menu handling
    - User interaction

    This is a SINGLE-RESPONSIBILITY class for a CLI calculator.
    """

    # CONSTRUCTOR METHOD
    def __init__(self):
        """
        Constructor method

        Automatically called when an object of the class is created.
        Initializes the calculator state.
        """
        self.history = []   # Stores calculation history

    def clear_screen(self):
        """Clears terminal screen for better UX"""
        print("\n" * 50)

    def safe_int(self, prompt=""):
        """Safely takes integer input from user"""
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid integer")
            return None

    def safe_float(self, prompt=""):
        """Safely takes float input from user"""
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number")
            return None

    def add_history(self, entry):
        """Adds an entry to calculation history"""
        self.history.append(entry)

    # BASIC OPERATION METHODS
    def addition(self, nums):
        """Adds multiple numbers"""
        return sum(float(i) for i in nums)

    def multiplication(self, nums):
        """Multiplies multiple numbers"""
        result = 1.0
        for i in nums:
            result *= float(i)
        return result

    def subtraction(self, a, b):
        """Subtracts two numbers"""
        return float(a) - float(b)

    def division(self, a, b):
        """Divides two numbers"""
        return float(a) / float(b)

    def modulus(self, a, b):
        """Finds modulus of two numbers"""
        return float(a) % float(b)

    def power(self, a, b):
        """Raises a number to a power"""
        return float(a) ** float(b)

    # MENU DISPLAY METHODS
    def main_menu(self):
        """Returns main menu string"""
        return """
════════════════════════════════════
   🧮 SCIENTIFIC CALCULATOR (OOP)
════════════════════════════════════
1. Basic Operations
2. Scientific Operations
3. Evaluate Expression
4. View History
5. Exit
════════════════════════════════════
"""

    def basic_menu(self):
        """Returns basic operations menu"""
        return """
--- BASIC OPERATIONS ---
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
0. Back to Main Menu
"""

    def scientific_menu(self):
        """Returns scientific operations menu"""
        return """
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

    # BASIC MENU CONTROLLER
    def run_basic(self):
        """Handles basic operations menu logic"""
        while True:
            self.clear_screen()
            print(self.basic_menu())

            choice = self.safe_int("Enter choice: ")
            if choice is None:
                continue

            if choice == 1:
                nums = input("Enter numbers separated by space: ").split()
                result = round(self.addition(nums), 6)
                self.add_history(f"{' + '.join(nums)} = {result}")
                print("Result:", result)

            elif choice == 2:
                nums = input("Enter two numbers: ").split()
                try:
                    result = round(self.subtraction(nums[0], nums[1]), 6)
                    self.add_history(f"{nums[0]} - {nums[1]} = {result}")
                    print("Result:", result)
                except:
                    print("❌ Invalid input")

            elif choice == 3:
                nums = input("Enter numbers separated by space: ").split()
                result = round(self.multiplication(nums), 6)
                self.add_history(f"{' * '.join(nums)} = {result}")
                print("Result:", result)

            elif choice == 4:
                nums = input("Enter two numbers: ").split()
                try:
                    a, b = float(nums[0]), float(nums[1])
                    if b == 0:
                        print("❌ Division by zero")
                        continue
                    result = round(self.division(a, b), 6)
                    self.add_history(f"{a} / {b} = {result}")
                    print("Result:", result)
                except:
                    print("❌ Invalid input")

            elif choice == 5:
                nums = input("Enter two numbers: ").split()
                try:
                    a, b = float(nums[0]), float(nums[1])
                    if b == 0:
                        print("❌ Modulus by zero")
                        continue
                    result = round(self.modulus(a, b), 6)
                    self.add_history(f"{a} % {b} = {result}")
                    print("Result:", result)
                except:
                    print("❌ Invalid input")

            elif choice == 6:
                nums = input("Enter base and power: ").split()
                try:
                    result = round(self.power(nums[0], nums[1]), 6)
                    self.add_history(f"{nums[0]} ** {nums[1]} = {result}")
                    print("Result:", result)
                except:
                    print("❌ Invalid input")

            elif choice == 0:
                break

            input("\nPress Enter to continue...")

    # SCIENTIFIC MENU CONTROLLER
    def run_scientific(self):
        """Handles scientific operations menu logic"""
        while True:
            self.clear_screen()
            print(self.scientific_menu())

            choice = self.safe_int("Enter choice: ")
            if choice is None:
                continue

            if choice == 1:
                x = self.safe_float("Enter x (>=0): ")
                if x is None or x < 0:
                    print("❌ Invalid input")
                    continue
                result = round(math.sqrt(x), 6)
                self.add_history(f"sqrt({x}) = {result}")
                print("Result:", result)

            elif choice == 2:
                nums = input("Enter base and power: ").split()
                try:
                    result = round(math.pow(float(nums[0]), float(nums[1])), 6)
                    self.add_history(f"{nums[0]} ^ {nums[1]} = {result}")
                    print("Result:", result)
                except:
                    print("❌ Invalid input")

            elif choice == 3:
                x = self.safe_float("Enter x (>0): ")
                if x is None or x <= 0:
                    print("❌ Invalid input")
                    continue
                result = round(math.log(x), 6)
                self.add_history(f"log({x}) = {result}")
                print("Result:", result)

            elif choice == 4:
                x = self.safe_float("Enter x (>0): ")
                if x is None or x <= 0:
                    print("❌ Invalid input")
                    continue
                result = round(math.log10(x), 6)
                self.add_history(f"log10({x}) = {result}")
                print("Result:", result)

            elif choice == 5:
                x = self.safe_float("Enter x: ")
                if x is None:
                    continue
                result = round(math.sin(x), 6)
                self.add_history(f"sin({x}) = {result}")
                print("Result:", result)

            elif choice == 6:
                x = self.safe_float("Enter x: ")
                if x is None:
                    continue
                result = round(math.cos(x), 6)
                self.add_history(f"cos({x}) = {result}")
                print("Result:", result)

            elif choice == 7:
                x = self.safe_float("Enter x: ")
                if x is None:
                    continue
                result = round(math.tan(x), 6)
                self.add_history(f"tan({x}) = {result}")
                print("Result:", result)

            elif choice == 8:
                x = self.safe_int("Enter integer x (>=0): ")
                if x is None or x < 0:
                    print("❌ Invalid input")
                    continue
                result = math.factorial(x)
                self.add_history(f"factorial({x}) = {result}")
                print("Result:", result)

            elif choice == 9:
                x = self.safe_float("Enter x: ")
                if x is None:
                    continue
                result = round(abs(x), 6)
                self.add_history(f"abs({x}) = {result}")
                print("Result:", result)

            elif choice == 10:
                x = self.safe_float("Enter x: ")
                if x is None:
                    continue
                result = round(math.exp(x), 6)
                self.add_history(f"e^{x} = {result}")
                print("Result:", result)

            elif choice == 0:
                break

            input("\nPress Enter to continue...")

    # EXPRESSION EVALUATION
    def evaluate_expression(self):
        """Evaluates a mathematical expression safely"""
        expression = input("Enter expression: ")

        forbidden = ["import", "__", "os", "sys", "open", "eval", "exec"]
        if any(word in expression for word in forbidden):
            print("❌ Invalid expression")
            return

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
            self.add_history(f"{expression} = {result}")
            print("Result:", result)
        except:
            print("❌ Invalid expression")

    # HISTORY VIEW
    def show_history(self):
        """Displays calculation history"""
        self.clear_screen()
        if not self.history:
            print("📭 No history yet")
        else:
            print("--- Calculation History ---")
            for i, item in enumerate(self.history, 1):
                print(f"{i}. {item}")
        input("\nPress Enter to continue...")

    # APPLICATION CONTROLLER
    def run(self):
        """Main application loop"""
        while True:
            self.clear_screen()
            print(self.main_menu())

            choice = self.safe_int("Enter choice: ")
            if choice is None:
                continue

            if choice == 1:
                self.run_basic()
            elif choice == 2:
                self.run_scientific()
            elif choice == 3:
                self.evaluate_expression()
                input("\nPress Enter to continue...")
            elif choice == 4:
                self.show_history()
            elif choice == 5:
                print("... See you soon again ...")
                break


# PROGRAM ENTRY POINT
if __name__ == "__main__":
    """
    This block ensures the program runs only
    when executed directly, not when imported.
    """
    app = ScientificCalculator()
    app.run()
