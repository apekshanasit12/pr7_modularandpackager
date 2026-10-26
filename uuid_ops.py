# Unique identifier generation (uses uuid module)
import uuid
from toolkit import file_ops


def menu():
    print("\nGenerate Unique Identifiers:")
    new_id = uuid.uuid4()
    print("\nGenerated UUID:", new_id)
    file_ops.save_log("Generated UUID: " + str(new_id))
    print("============================")


if __name__ == "__main__":
    menu()
