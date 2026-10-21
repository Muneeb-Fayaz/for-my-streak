class Employee:
    id:int
    name:str

    def __init__(self,a,b):
        self.id=a
        self.name=b


e1=Employee(1,"muneeb")
e2=Employee(2,"rayees")

print(e1.id)
print(e1.name)

print(e2.id)
print(e2.name)
