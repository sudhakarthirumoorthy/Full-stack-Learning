
# try:
#     num = int(input("Enter a number: "))
#     print("Your number is:", num)

# except ValueError:
#     print("Please enter numbers only!")


try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

except ValueError as error:
    print("Error:", error)

else:
    print("Your age is:", age)

finally:
    print("Program completed.")