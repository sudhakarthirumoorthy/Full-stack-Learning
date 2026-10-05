name = input("Enter a string: ")

count = 0

for character in name:
    if character in "aeiou":
        count = count + 1

print("Number of vowels:", count)