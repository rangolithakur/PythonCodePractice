from datetime import date

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def fromBirthYear(cls,name,birthyear):
        return cls(name,date.today().year-birthyear)

    def display(self):
        print(self.name,'age is', str(self.age))

p=Person('Rangoli',19)
p.display()

q = p.fromBirthYear('Thakur',1989)
q.display()

