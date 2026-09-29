# # operators
# # arithmetic operator
# a=10
# b=5
# print(a+b)
# # Assignment operator

# # input and output

# name = input("Enter your name: ")
# # print("hello, " + name + "! Welcome to the program.")
# print(f"Hello, {name}! Welcome to the program.")

# # sep
# print("Hello", "World", sep=" - ")

# # end
# print("Hello", "world", end="")

# # Conditional Statements

# user_name = input("Enter your name: ") 
# if user_name == "maari":
#     print(f"Hello, {user_name}! Welcome to the program.")
# elif user_name == "arun":
#     print(f"Hello, {user_name}! Welcome to the program.")
# else:
#     print("none")

#     status = input("Enter your status (active/inactive): ")
#     if status == "active":
#         print("You are active.")
#     elif status == "inactive":
#         print("You are inactive.")
        
day = 5

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")