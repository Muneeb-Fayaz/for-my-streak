num = int(input("Enter a number: "))        # to check if a number is a three-digit number

if num >= 100:
    if num <= 999:
        print("The number is a three-digit number.")
    else:
        print("The number is not a three-digit number.")
elif num <= -100:
    if num >= -999:
        print("The number is a three-digit number.")
    else:
        print("The number is not a three-digit number.")
else:
    print("The number is not a three-digit number.")