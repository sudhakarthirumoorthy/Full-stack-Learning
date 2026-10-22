name = input("Enter a string: ")

count = 0

for character in name:
    if character in "aeiou":
        print(character)
        count += 1

print("Number of vowels:", count)