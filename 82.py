class Employee:
    id:int
    name:str
    name:int
    sal:int
    ta:int
    da:int
    ts:int

    def __init__(self,a,b,c,d,e,f):
        self.id=a
        self.name=b
        self.sal=c
        self.ta=d
        self.da=e
        self.tax=f

    def calc(self):
            self.ts= self.sal+self.ta+self.da

    def display(self):
        print(self.id)
        print(self.name)
        print(self.ts)

e1=Employee(1,"muneeb",1000,200,100)
e2=Employee(2, "rayees",50000,3000,20000)
e3=Employee(3,"tahleel",10000,2000,3000)
e4=Employee(3,"wasif",2000000,50000,30000,)

e1.calc()
e2.calc()
e3.calc()
e4.calc()

e1.display()
e2.display()
e3.display()
e4.display()
