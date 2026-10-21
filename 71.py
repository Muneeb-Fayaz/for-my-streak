def sum():
    x=10
    y=20
    z=x+y
    print(z)

def even():
    x=0
    while x<10:
        print(x)
        x=x+2

def odd():
    x=1
    while x<10:
        print(x)
        x=x+2

def series():
    x=1
    while x<10:
        print(x)
        x=x+1

def factr():
    x=5 
    f=1
    while x>0:
        f=x*f
        x=x-1
        print(f)

def square():
    x=1
    y=1
    while x<6:
        print(y)
        x=x+1
        y=x*x  

def cube():
    x=1
    y=1
    while x<6:
        print(y)
        x=x+1
        y=x*x*x

def atm():
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


def greater():
    x=input ("enter value of x:-")
    x=int(x)

    y=input ("enter value of y:-")
    y=int(y)

    if x<y:
        print("y is greater")
    elif x>y:
        print("x is greater")
    else:
        print("x=y")

def reverse():
    x=123
    s=0
    while x>0:
        y=x%10
        s=s*10+y
        x=x//10
    print(s)


while 1:
    print("Enter choice")
    print("1 for sum")
    print("2 for even")
    print("3 for odd")
    print("4 for series")
    print("5 for factorial")
    print("6 for square")
    print("7 for cube")
    print("8 for atm")
    print("9 for greater")
    print("10 for reverse 123")
    c=input("Please enter ,")
    c=int(c)

    if c==1:
        sum()
    elif c==2:
        even()
    elif c==3:
        odd()
    elif c==4:
        series()
    elif c==5:
        factr()
    elif c==6:
        square()
    elif c==7:
        cube()
    elif c==8:
        atm()
    elif c==9:
        greater()
    elif c==10:
        reverse()
    else:
        print("wrong choice")
    print("end")