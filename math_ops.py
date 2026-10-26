# Mathematical operations (uses math module)
import math
from toolkit import file_ops


def factorial():
    try:
        n = int(input("\nEnter a number: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            text = "Factorial: " + str(math.factorial(n))
            print(text)
            file_ops.save_log(text)
    except ValueError:
        print("Please enter a valid whole number!")


def compound_interest():
    try:
        p = float(input("\nEnter principal amount: "))
        r = float(input("Enter rate of interest (in %): "))
        t = float(input("Enter time (in years): "))
        amount = p * (1 + r / 100) ** t
        text = "Compound Interest: {:.2f}".format(amount)
        print(text)
        file_ops.save_log(text)
    except ValueError:
        print("Please enter valid numbers!")


def trigonometry():
    try:
        angle = float(input("\nEnter angle in degrees: "))
        rad = math.radians(angle)
        text = "sin: {:.4f}, cos: {:.4f}, tan: {:.4f}".format(math.sin(rad), math.cos(rad), math.tan(rad))
        print(text)
        file_ops.save_log("Trigonometry of " + str(angle) + " degrees -> " + text)
    except ValueError:
        print("Please enter a valid number!")


def area_of_shapes():
    print("\n1. Circle  2. Rectangle  3. Triangle  4. Square")
    shape = input("Choose a shape: ")
    area = None
    try:
        if shape == "1":
            r = float(input("Enter radius: "))
            area = math.pi * r ** 2
        elif shape == "2":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            area = l * w
        elif shape == "3":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            area = 0.5 * b * h
        elif shape == "4":
            s = float(input("Enter side: "))
            area = s * s
        else:
            print("Invalid shape choice!")
        if area is not None:
            text = "Area: {:.2f}".format(area)
            print(text)
            file_ops.save_log(text)
    except ValueError:
        print("Please enter valid numbers!")


def logarithm():
    try:
        n = float(input("\nEnter a number: "))
        if n <= 0:
            print("Logarithm is only defined for positive numbers.")
            return
        text = "Natural log (ln): {:.4f}, log base 10: {:.4f}, log base 2: {:.4f}".format(
            math.log(n), math.log10(n), math.log2(n))
        print(text)
        file_ops.save_log("Logarithm of " + str(n) + " -> " + text)
    except ValueError:
        print("Please enter a valid number!")


def basic_arithmetic():
    try:
        a = float(input("\nEnter first number: "))
        b = float(input("Enter second number: "))
        lines = ["Addition: " + str(a + b),
                 "Subtraction: " + str(a - b),
                 "Multiplication: " + str(a * b)]
        if b != 0:
            lines.append("Division: " + str(a / b))
        else:
            lines.append("Division: not possible (divide by zero)")
        lines.append("Power: " + str(math.pow(a, b)))
        for line in lines:
            print(line)
            file_ops.save_log(line)
    except (ValueError, OverflowError):
        print("Please enter valid numbers!")


def menu():
    print("\nMathematical Operations:")
    print("1. Calculate Factorial")
    print("2. Solve Compound Interest")
    print("3. Trigonometric Calculations")
    print("4. Area of Geometric Shapes")
    print("5. Logarithm")
    print("6. Basic Arithmetic")
    print("7. Back to Main Menu")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            factorial()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            trigonometry()
        elif choice == "4":
            area_of_shapes()
        elif choice == "5":
            logarithm()
        elif choice == "6":
            basic_arithmetic()
        elif choice == "7":
            break
        else:
            print("Invalid choice! Try again.")
        print("============================")


if __name__ == "__main__":
    menu()
