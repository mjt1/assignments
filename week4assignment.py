def read_and_modify_file():
    filename = input("Enter the filename to read: ")
    
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    # Modify content (example: convert text to uppercase)
    modified_content = content.lower()

    new_filename = "modified_" + filename
    try:
        with open(new_filename, "w") as file:
            file.write(modified_content)
        print(f"Modified content written to '{new_filename}'")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Run the function
read_and_modify_file()
