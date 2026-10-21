for a in range (100,500,1):    #outer for loop
    t = a
    s = 0                    #s=sum of digits
    while t > 0:             #inner loop
        digit = t % 10
        s += digit ** 3
        t = t // 10
    if s == a:               #if condtion 
        print(a)
    a += 1

