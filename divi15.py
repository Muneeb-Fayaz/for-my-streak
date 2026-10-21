num = 1
while num <= 50:                            #outer loop   # check div by 3 using digit sum
    
    temp = num  
    sum_d = 0
    while temp > 0:                         #inner loop
        digit = temp % 10
        sum_d += digit
        temp //= 10
    div_by_3 = (sum_d % 3 == 0)             # check div by 5

    div_by_5 = (num % 5 == 0)
    if div_by_3:
        if div_by_5:
            print("code today")
        else:
            print("code")
    elif div_by_5:
        print("today")
    else:
        print(num)
    num += 1
