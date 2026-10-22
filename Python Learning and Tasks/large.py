numbers = [10, 50, 20, 40]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)