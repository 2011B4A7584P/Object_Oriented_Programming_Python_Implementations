class Employee:

    w_hrs = 40

    def __init__(self, name, age, sales):
        self.name = name
        # age = 30
        # this restricts the lifespan of age attribute
        # to this method only

        # self.age = 30
        # this hard codes the value of age parameter
        self.age = age
        self.sales = sales

    def has_achieved_target(self):
        return self.sales > 5

    # a pure static method to be used by class name only
    def welcome():
        print("Welcome to Wonderland")

    @staticmethod
    def welcome_message():
        print("Welcome to Wonderland")

    def details(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Sales : ", self.sales)

    def change_w_hrs(self):
        self.w_hrs = 55


if __name__ == '__main__':

    emp_1 = Employee("Ben", 23, 3)
    emp_2 = Employee("Mary", 17, 7)

    print(emp_1.name)
    print(emp_1.w_hrs)
    print(emp_1.has_achieved_target())
    print(emp_2.name)
    print(emp_2.w_hrs)
    print(emp_2.has_achieved_target())

    emp_1.w_hrs = 45

    print(emp_1.w_hrs)
    print(emp_2.w_hrs)

    Employee.w_hrs = 50
    # delattr(emp_1, "w_hrs")
    # del(emp_1.w_hrs)
    print(emp_1.w_hrs)
    print(emp_2.w_hrs)

    emp_1.details()
    emp_2.details()

    Employee.welcome()

    emp_1.welcome_message()
    emp_2.welcome_message()

    print(emp_1.w_hrs)
    emp_1.change_w_hrs()
    print(emp_1.w_hrs)
    print(emp_2.w_hrs)
    print(Employee.w_hrs)