class Employee:
    id:int
    name:str

    def __init__(self,a,b):
        self.id=a
        self.name=b

    def display(self):
        print(self.id)
        print(self.name)


e1=Employee(1,"muneeb")
e2=Employee(2,"rayees")
 
e1.display()
e2.display()