num1 = 8
print("Input the number that will divide:")
num2 = int(input())

try:
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("We can't divide by zero")
except TypeError:
    print("Your input value must be an integer")
print("Tarraah, Program keeps running")