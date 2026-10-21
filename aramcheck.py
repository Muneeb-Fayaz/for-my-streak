a = 100
while a <= 500:              #outer loop
    t = a
    s = 0                    #s=sum of digits
    while t > 0:             #inner loop
        digit = t % 10
        s += digit ** 3
        t = t // 10
    if s == a:               #if condtion 
        print(a)
    a += 1

