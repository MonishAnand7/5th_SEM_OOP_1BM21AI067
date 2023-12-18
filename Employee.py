class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary 

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def work(self):
        print(f"{self.name} is working.")

    def show(self):
        print(f"Name: {self.name}")
        print(f"Salary: Rs.{self.__salary}")

name=input("enter the name:")
sal=int(input("enter initial salary:"))
emp = Employee(name,sal)

emp.show() 
new_sal=int(input("enter the new salary:"))
emp.set_salary(new_sal)

print(f"Updated Salary: Rs.{emp.get_salary()}")

emp.work()
