# Random data generation (uses random and string modules)
import random
import string
from toolkit import file_ops


def random_number():
    try:
        low = int(input("\nEnter minimum value: "))
        high = int(input("Enter maximum value: "))
        number = random.randint(low, high)
        print("Random Number:", number)
        file_ops.save_log("Random Number: " + str(number))
    except ValueError:
        print("Please enter valid whole numbers! (minimum must not be bigger than maximum)")


def random_list():
    try:
        size = int(input("\nEnter list size: "))
        low = int(input("Enter minimum value: "))
        high = int(input("Enter maximum value: "))
        numbers = [random.randint(low, high) for _ in range(size)]
        print("Random List:", numbers)
        file_ops.save_log("Random List: " + str(numbers))
    except ValueError:
        print("Please enter valid whole numbers!")


def random_password():
    try:
        length = int(input("\nEnter password length: "))
        characters = string.ascii_letters + string.digits + "!@#$%&*"
        password = ""
        for _ in range(length):
            password += random.choice(characters)
        print("Generated Password:", password)
        file_ops.save_log("Generated Password: " + password)
    except ValueError:
        print("Please enter a valid number!")


def random_otp():
    otp = ""
    for _ in range(6):
        otp += str(random.randint(0, 9))
    print("\nGenerated OTP:", otp)
    file_ops.save_log("Generated OTP: " + otp)


def menu():
    print("\nRandom Data Generation:")
    print("1. Generate Random Number")
    print("2. Generate Random List")
    print("3. Create Random Password")
    print("4. Generate Random OTP")
    print("5. Back to Main Menu")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            random_number()
        elif choice == "2":
            random_list()
        elif choice == "3":
            random_password()
        elif choice == "4":
            random_otp()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")
        print("============================")


if __name__ == "__main__":
    menu()
