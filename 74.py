def add():
    x=input("enter no.")
    x=int(x)
    arr.append(x)
    print("element added")

def disp():
    if len(arr)>0:
        i=len(arr)
        i=i-1
        while i>=0:
            print(arr[i])
            i=i-1
    else:
        print("empty")

arr=[]
add()
add()
add()
add()
add()
add()
disp()
