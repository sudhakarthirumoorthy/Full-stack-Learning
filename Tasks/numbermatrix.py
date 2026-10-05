rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range(rows):
    for j in range(3, columns + 1):
        print(j, end=" ")
    print()

# Outer loop → controls ROWS
# Inner loop → controls NUMBERS inside each ROW
# print()    → moves to the next ROW