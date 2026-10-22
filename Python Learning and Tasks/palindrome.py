name = input("Enter a string: ")

reverse_name = name[::-1]

if name == reverse_name:
    print(name, "is a palindrome")
else:
    print(name, "is not a palindrome")