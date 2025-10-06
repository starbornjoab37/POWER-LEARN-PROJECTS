
#Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
file = input("Enter the filename to read: ")
try:
    with open(file, "r") as infile:
        content = infile.read()
    modified_content = content.upper()  # Example modification: convert to uppercase
    with open("modified_" + file, "w") as outfile:
        outfile.write(modified_content) 
except FileNotFoundError:
    print("File not found.")

#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

filename = input("Enter the filename to read: ")
try:
    with open(filename, "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error reading file:", e)
