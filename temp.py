import os

def print_folder_structure(folder_path, indent=0):
    # Print the current folder
    print(" " * indent + f"|-- {os.path.basename(folder_path)}")
    try:
        # Iterate through the directory contents
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                # If item is a directory, recurse
                print_folder_structure(item_path, indent + 4)
            else:
                # If item is a file, print its name
                print(" " * (indent + 4) + f"|-- {item}")
    except PermissionError:
        # Handle folders you may not have permission to access
        print(" " * (indent + 4) + "|-- [Access Denied]")

# Specify the folder path you want to display
folder_path = "./"  # Current directory or replace with your folder path
print_folder_structure(folder_path)