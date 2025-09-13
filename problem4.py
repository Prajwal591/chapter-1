import os

def list_directory_contents(path):
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
        return
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
        return
    except PermissionError:
        print(f"Error: No permission to read directory '{path}'.")
        return

    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            print(f"[DIR]  {entry}")
        elif os.path.isfile(full_path):
            print(f"[FILE] {entry}")
        else:
            print(f"[OTHER] {entry}")

if __name__ == "__main__":
    directory = input("Enter directory path: ")
    list_directory_contents(directory)
