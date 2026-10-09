def numbers():
    for i in range(1, 11):
        print(i)

numbers()

def even_numbers():
    for i in range(1,21):
        if i % 2 == 0:
            print(i)

even_numbers()

def table(number):
    for i in range(1,11):
        print(i, "X", number, "=", number*i)
table(8)

def total():
    result = 0

    for i in range(1,11):
        result = result + i
    return result

answer = total()
print("Total", answer)

# def factorial(number):
#     for i in range(1,6):
#     return i* number
# factorial(5)
# print("Toatl", answer)

def factorial(number):
    result = 1

    for i in range(1,6):
        result = result * i

    return result


answer = factorial(5)
print("Factorial:", answer)