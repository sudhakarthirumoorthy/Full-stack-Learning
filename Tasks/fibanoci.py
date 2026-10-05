num = int(input("Enter the number of terms: "))

first = 0
second = 1

for i in range(num):
    print(first, end="\n")

    next_number = first + second
    first = second
    second = next_number

# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones
# Fibonacci series: Each next number is calculated by adding the previous two numbers.
# first + second = next number, then first and second are moved forward for the next calculation.