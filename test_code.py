import math

def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    avg = total / len(numbers)
    return avg

def find_max(numbers):
    
    x = 0
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max

def unused_function():
    x = 10
    y = 20
    z = x + y

numbers = [10,20,30,40]

print("Average:", calculate_average(numbers))
print("Max:", find_max(numbers))
