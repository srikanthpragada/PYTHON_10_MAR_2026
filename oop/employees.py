from abc import ABC, abstractmethod

# Abstract class
class Employee (ABC):
    def __init__(self, name, desg):
        self.name = name
        self.desg = desg

    def set_desg(self, newdesg):
        self.desg = newdesg

    def show(self):
        print(self.name)
        print(self.desg)

    # Abstract Method
    @abstractmethod
    def get_salary(self):
        pass



class RegularEmployee(Employee):
    def __init__(self, name, desg, salary):
        super().__init__(name, desg)
        self.salary = salary

    def show(self):
        super().show()
        print(self.salary)

    def get_salary(self):
        return self.salary


class Consultant(Employee):
    def __init__(self, name, desg, hours, rate):
        super().__init__(name, desg)
        self.hours = hours
        self.rate = rate

    def show(self):
        super().show()
        print(self.hours)
        print(self.rate)

    def get_salary(self):
        return self.hours * self.rate

    def set_rate(self, rate):
        self.rate = rate

    def set_hours(self, hours):
        self.hours = hours

#e = Employee("", "")


r = RegularEmployee("Scott", "Programmer", 100000)
r.set_desg("Sr. Programmer")
r.show()

c = Consultant("Jason", "DBA", 10, 1000)
c.set_rate(2000)
c.show()
print(c.get_salary())
