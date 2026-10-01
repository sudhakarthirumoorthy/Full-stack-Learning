name = input("Enter a string: ")

count = 0

for character in name:
    if character in "aeiou]:
        count = count + 1

print("Number of vowels:", count)
a = "the whole while the"
print(a.count("the"))
print(a.replace("the", "THE"))
print(a.split(" "))
print(len(a.split(" ")))
print(a.rstrip("-"))

email = "  Sudhakar@Tghirum@ooo.COM  "
print(email.partition("a"))
print(email.rpartition("a"))