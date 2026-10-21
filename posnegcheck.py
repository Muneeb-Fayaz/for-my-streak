num = int(input("Enter a number: "))  # Program to check if a number is positive/negative and even/odd

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif num < 0:
    if num % 2 == 0:
        print("The number is negative and even.")
    else:
        print("The number is negative and odd.")
else:
    print("The number is zero, which is even.")
