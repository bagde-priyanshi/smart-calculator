import operator
import math

history = []  # Stores calculation history

def main_menu():
    print("-"*50)
    print("         Welcome to Smart Calculator      ")
    print("-"*50)
    print("1. Basic Arithmetic (+, -, *, /, %, **)")
    print("2. Scientific Functions (sqrt, factorial, log, sin, cos, tan, abs)")
    print("3. View Calculation History")
    print("4. Exit")

# --- BASIC ARITHMETIC ---
def basic_arithmetic():
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "%": operator.mod,
        "**": operator.pow
    }

    try:
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        op = input("Enter operator (+, -, *, /, %, **): ").strip()
        
        if op not in ops:
            print("Invalid operator.")
            return
        
        if op in ["/", "%"] and num2 == 0:
            raise ZeroDivisionError
        
        result = round(ops[op](num1, num2), 6)  
        print(f"{num1} {op} {num2} = {result}")
        history.append(f"{num1} {op} {num2} = {result}")

    except ValueError:
        print("Invalid number entered.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

# --- SCIENTIFIC FUNCTIONS ---
def scientific_functions():
    print("\nScientific Options:")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Logarithm")
    print("4. Sine")
    print("5. Cosine")
    print("6. Tangent")
    print("7. Absolute Value")
    
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            num = float(input("Enter number: "))
            if num < 0:
                print("Cannot take square root of negative number.")
                return
            result = round(math.sqrt(num), 6)       
            print(f"√{num} = {result}")
            history.append(f"√{num} = {result}")

        elif choice == 2:
            num = int(input("Enter number: "))
            if num < 0:
                print("Factorial not defined for negative numbers.")
                return
            result = math.factorial(num)
            print(f"{num}! = {result}")
            history.append(f"{num}! = {result}")

        elif choice == 3:
            num = float(input("Enter number: "))
            if num <= 0:
                print("Logarithm undefined for zero or negative numbers.")
                return
            base = float(input("Enter base (default 10): ") or 10)
            result = math.log(num, base)
            print(f"log base {base} of {num} = {result}")
            history.append(f"log base {base} of {num} = {result}")

        elif choice == 4:
            angle = float(input("Enter angle in degrees: "))
            result = math.sin(math.radians(angle))
            print(f"sin({angle}) = {result}")
            history.append(f"sin({angle}) = {result}")

        elif choice == 5:
            angle = float(input("Enter angle in degrees: "))
            result = math.cos(math.radians(angle))
            print(f"cos({angle}) = {result}")
            history.append(f"cos({angle}) = {result}")

        elif choice == 6:
            angle = float(input("Enter angle in degrees: "))
            result = math.tan(math.radians(angle))
            print(f"tan({angle}) = {result}")
            history.append(f"tan({angle}) = {result}")

        elif choice == 7:
            num = float(input("Enter number: "))
            result = abs(num)
            print(f"|{num}| = {result}")
            history.append(f"|{num}| = {result}")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input.")

# --- VIEW HISTORY ---
def view_history():
    if not history:
        print("No calculations yet.")
    else:
        print("\nCalculation History:")
        for i, calc in enumerate(history, 1):   # adds numbering
            print(f"{i}. {calc}")
        clear = input("\nClear history? (y/n): ")
        if clear.lower() == 'y':
            history.clear()
            print("History cleared.")

# --- MAIN LOOP ---
while True:
    main_menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            basic_arithmetic()
        elif choice == 2:
            scientific_functions()
        elif choice == 3:
            view_history()
        elif choice == 4:
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")
