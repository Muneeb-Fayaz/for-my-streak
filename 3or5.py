# num = int(input("Enter a number: "))    # enter the value for number to which we have to check the number is positve or negative    

# if num % 3 == 0:
#     print("The number is divisible by 3 .")
# if num % 5 == 0:
#     print("The number is divisible by 5 .")
# else:
#     print("The number is not divisible by 3 or 5.")

num = int(input("Enter a number: "))

if num % 3 == 0:
    if num % 5 == 0:
        print("The number is divisible by both 3 and 5.")
    else:
        print("The number is divisible by 3.")
elif num % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 3 or 5.")
