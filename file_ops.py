# File operations - our own custom module
import datetime

LOG_FILE = "toolkit_log.txt"


def save_log(message):
    """Saves every output of the toolkit into a text file with a timestamp."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = open(LOG_FILE, "a")
    file.write("[" + now + "] " + message + "\n")
    file.close()


def create_file():
    name = input("\nEnter file name: ")
    file = open(name, "w")
    file.close()
    print("File created successfully!")


def write_file():
    name = input("\nEnter file name: ")
    data = input("Enter data to write: ")
    file = open(name, "w")
    file.write(data)
    file.close()
    print("Data written successfully!")


def read_file():
    name = input("\nEnter file name: ")
    try:
        file = open(name, "r")
        print("File Content:")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("File not found!")


def append_file():
    name = input("\nEnter file name: ")
    data = input("Enter data to append: ")
    file = open(name, "a")
    file.write("\n" + data)
    file.close()
    print("Data appended successfully!")


def menu():
    print("\nFile Operations:")
    print("1. Create a new file")
    print("2. Write to a file")
    print("3. Read from a file")
    print("4. Append to a file")
    print("5. Back to Main Menu")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            append_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")
        print("============================")


if __name__ == "__main__":
    menu()
