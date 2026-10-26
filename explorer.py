# Explore module attributes using dir()
import importlib
from toolkit import file_ops


def menu():
    print("\nExplore Module Attributes:")
    name = input("Enter module name to explore: ")
    try:
        module = importlib.import_module(name)
        attributes = [a for a in dir(module) if not a.startswith("_")]
        print("Available Attributes in", name, "module:")
        print(attributes)
        file_ops.save_log("Explored module " + name + ": " + str(len(attributes)) + " attributes found")
    except ImportError:
        print("Module not found!")
    print("============================")


if __name__ == "__main__":
    menu()
