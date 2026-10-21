class Student:
    id:int
    sal:int
    def __init__(self,a,b):
        self.id=a
        self.sal=b

arr=[
Student(1,60),
Student(2,30),
Student(3,40)
]

print(arr[0].id)
print(arr[0].sal)

print(arr[1].id)
print(arr[1].sal)

print(arr[2].id)
print(arr[2].sal)


