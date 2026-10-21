class Student:
    id:int
    sal:int

obj=Student()
temp=input("enter id:")
tem=int(temp)

obj.id=temp

temp= input("enter sal:")
temp=int(temp)

obj.sal=temp 

print(obj.id)
print(obj.sal)