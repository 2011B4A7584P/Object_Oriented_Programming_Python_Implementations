class Employee:
    name = 'Ashish'

    @staticmethod
    def change_name():
        Employee.name = 'Ashu'


if __name__ == "__main__":
    employee = Employee()
    print(employee.name)
    Employee.change_name()
    print(employee.name)
