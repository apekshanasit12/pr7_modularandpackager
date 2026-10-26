# Datetime and Time operations (uses datetime and time modules)
import datetime
import time
from toolkit import file_ops


def show_current_datetime():
    now = datetime.datetime.now()
    text = now.strftime("%Y-%m-%d %H:%M:%S")
    print("\nCurrent Date and Time:", text)
    file_ops.save_log("Current Date and Time: " + text)


def date_difference():
    print("\nYou can enter a date (YYYY-MM-DD) or date with time (YYYY-MM-DD HH:MM:SS)")
    d1 = input("Enter the first date/time: ")
    d2 = input("Enter the second date/time: ")
    try:
        first = parse_date(d1)
        second = parse_date(d2)
        diff = abs(second - first)
        text = "Difference: " + str(diff.days) + " days " + str(diff.seconds // 3600) + " hours " + str((diff.seconds % 3600) // 60) + " minutes"
        print(text)
        file_ops.save_log(text)
    except ValueError:
        print("Invalid format! Use YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.")


def parse_date(text):
    # try date with time first, then only date
    try:
        return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return datetime.datetime.strptime(text, "%Y-%m-%d")


def custom_format():
    d = input("\nEnter a date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(d, "%Y-%m-%d")
        print("Examples of format codes: %d-%m-%Y, %B %d, %Y, %A, %d %b %y")
        fmt = input("Enter your format: ")
        text = "Formatted Date: " + date.strftime(fmt)
        print(text)
        file_ops.save_log(text)
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")


def stopwatch():
    input("\nPress Enter to start the stopwatch...")
    start = time.time()
    input("Press Enter to stop the stopwatch...")
    end = time.time()
    text = "Elapsed Time: " + str(round(end - start, 2)) + " seconds"
    print(text)
    file_ops.save_log(text)


def countdown_timer():
    try:
        seconds = int(input("\nEnter time in seconds: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    total = seconds
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
    file_ops.save_log("Countdown of " + str(total) + " seconds completed")


def working_hours():
    # uses the time module to convert HH:MM into seconds
    start = input("\nEnter start time (HH:MM, 24-hour): ")
    end = input("Enter end time (HH:MM, 24-hour): ")
    try:
        t1 = time.mktime(time.strptime("2000-01-01 " + start, "%Y-%m-%d %H:%M"))
        t2 = time.mktime(time.strptime("2000-01-01 " + end, "%Y-%m-%d %H:%M"))
        if t2 < t1:
            print("End time must be after start time!")
            return
        hours = (t2 - t1) / 3600
        text = "Working Hours: " + str(round(hours, 2)) + " hours"
        print(text)
        file_ops.save_log(text)
    except ValueError:
        print("Invalid time format! Use HH:MM.")


def menu():
    print("\nDatetime and Time Operations:")
    print("1. Display current date and time")
    print("2. Calculate difference between two dates/times")
    print("3. Format date into custom format")
    print("4. Stopwatch")
    print("5. Countdown Timer")
    print("6. Calculate Working Hours")
    print("7. Back to Main Menu")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            show_current_datetime()
        elif choice == "2":
            date_difference()
        elif choice == "3":
            custom_format()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown_timer()
        elif choice == "6":
            working_hours()
        elif choice == "7":
            break
        else:
            print("Invalid choice! Try again.")
        print("============================")



if __name__ == "__main__":
    menu()
