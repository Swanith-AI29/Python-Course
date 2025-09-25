class person() :
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print('Name-',self.name)
        print('ID numberself',self.idnumber)
class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
        print('salary-',self.salary)
        print('Post-',self.post)
person1=employee("Vachan",347,45000,'assistant manager')
person1.display()