amount =input("Enter amount: ")
amount=int(amount)
n2000 = 0
n1000 = 0
n500 = 0
n200 = 0
n100 = 0


if amount >= 2000:
    n2000 = amount // 2000      
    amount = amount - (n2000 * 2000) 

if amount >= 1000:
    n1000 = amount // 1000
    amount = amount - (n1000 * 1000)

if amount >= 500:
    n500 = amount // 500
    amount = amount - (n500 * 500)

if amount >= 200:
    n200 = amount // 200
    amount = amount - (n200 * 200)

if amount >= 100:
    n100 = amount // 100
    amount = amount - (n100 * 100)


print("2000 notes:", n2000)
print("1000 notes:", n1000)
print("500 notes :", n500)
print("200 notes :", n200)
print("100 notes :", n100)

