class employee:
    def __init__ (self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    
    def totalSalary(self, target):
        totalsalary = self.salary + target
        print ("total salary:" ,totalsalary)
     
    def printAll(self):
        print("name:" ,self.name)
        print("age:" ,self.age)
        print("salary:" ,self.salary)
        
em1 = employee ("asmaa", 24, 90000)
em1.printAll()
em1.totalSalary(1000)
print("\n")
em2 = employee ("ali",22,50000)
em2.printAll()
em2.totalSalary(2000)
print("\n")
em3 = employee ("noha", 27, 100000)
em3.printAll()
em3.totalSalary(2000)