def add():
    x=input("enter number.")
    x=int(x)
    arr.append(x)
    print("element added")


def disp():
    if len(arr)>0:
        
        for a in arr:
            print(a)
    else:
        print("empty")

def popit():            # to remove element 
    if len(arr)>=0:
        arr.pop(0)
        print("element removed")
    else:
        print("empty")

arr=[]

while True:

    print("enter 1 for add  ")
    print("enter 2 for display ")
    print("enter 3 for remove ")


    c=input ("please enter")

    c=int(c)
    if c==1:
        add()
    elif c==2:
        disp()
    elif c==3:
        popit()
    else :
        print ("wrong choice")