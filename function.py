# Function To Determine whether number is even or not
def isEven(x):
    if (x % 2 == 0):
        return True
    else:
        return False


# Ask user to enter a number
print("Input a number:")
my_number = int(input())

if isEven(my_number):
   print("The number is even")
else:
   print("The number is odd")
