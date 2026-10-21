array = [1, 2, 3, 4, 5, 6, 7, 8, 13, 19, 23, 25, 26]

prime_count = 0

for num in array:
    if num >= 2:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, "is prime")
            prime_count = prime_count+1

print("Total number of prime numbers:", prime_count)