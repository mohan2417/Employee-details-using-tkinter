class Details:
    def get_details(self):
        print("***********************Employee details*****************************")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        department = input("Enter Department: ").upper()
        salary = float(input("Enter Salary: "))
        emp_id=input("Enter ID: ")
        return name, age, gender, department, salary,emp_id


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_person_details(self):
        print("****************************************Person Details*********************************************************")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Gender : {self.gender}")


class Employee(Person,Details):
    def __init__(self, name, age, gender, department, salary, emp_id):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display_employee_details(self):
        self.display_person_details()
        print("****************************Employee Details********************************")
        print(f"Employee ID : {self.emp_id}")
        print(f"Department  : {self.department}")
        print(f"Salary      :{self.salary} Rs")


while True:
    d = Details()
    name, age, gender, emp_id, department, salary = d.get_details()

    emp = Employee(name, age, gender, emp_id, department, salary)
    emp.display_employee_details()

    again = input("\nDo you want to enter another employee's details? (yes/no): ").lower()
    if again != "yes":
        print("\nTHANK YOU !!!")
        break
