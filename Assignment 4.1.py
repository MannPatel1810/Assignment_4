# Task 1 : Read a file and Handle Errors

try:
    # Open and read the file
    file = open("sample.txt", "r")

    # Read and print file content line by line
    print(" Reading file contents :")
    for line in file:
        print(line.strip())

    # Close the file
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

except Exception as e:
    print("An unexpected error occurred:", e)
