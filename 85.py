class Student:
    id:int
    sal:int

    def __init__(self,a,b):
        self.id=a
        self.sal=b


arr=[
    Student(1,60),
    Student(2,40)
    ]


for a in arr:
    print(a.id)
    print(a.sal)
