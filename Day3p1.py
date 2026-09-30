
# for loop
i=100
for i in range(100):
    print(i)

# while loop
i=1
while i<=10:
    print(i)
    i+=1
print(i)

for i in range(1,5):
    for j in range(3,5):
        print("*", end=" ")
    print()

    # continue statement
    for i in range(1, 6):
    if i == 3:
        continue

    print(i)

    # break statement
    for i in range(1, 10):
    if i == 5:
        break

    print(i)