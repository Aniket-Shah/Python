class Emp:              #Blank Form
    def __init__(self,name,salary):     #Consturctor
        self.name = name
        self.salary = salary
    def getSalary(self):
            return self.salary

e1 = Emp("Aniket", 50000) #Object
print(e1.salary)
print(e1.name)
# e1.getSalary()


e2 = Emp("Ansh", 45000) #Object
print(e2.salary)
print(e2.name)