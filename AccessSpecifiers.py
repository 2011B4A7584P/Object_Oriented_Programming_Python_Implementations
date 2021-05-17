class Company:

    # public variable
    # meant to be visible to everyone

    welcomeMessage = 'Welcome to the corporate world!'
    print(welcomeMessage)

    # a protected variable
    # meant for the class and it's subclasses
    _budget = '80 Billion'

    # a private variable
    # meant strictly for the class only
    __profit = '30 Million'

    def __init__(self, name):
        self.name = name

    def company_details(self):
        print('Company Details :')

        print('Company Name : ', self.name)
        print('Company Budget : ', self._budget)
        print('Company Profit : ', self.__profit)


if __name__ == '__main__':

    company = Company('Citi')
    company.company_details()
    print(company._budget)
    # print(company.__profit)
    print(company._Company__profit)