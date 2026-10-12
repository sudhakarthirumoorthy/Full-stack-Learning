
# 1. Write the function into a file
with open("message.html", "w") as file:
    file.write("def welcome():\n")
    file.write('    print("Welcome to Python!")\n')

# 2. Read the function from the file
with open("message.txt", "r") as file:
    code = file.read()

# 3. Execute the function definition
exec(code)

# 4. Call the function
welcome()