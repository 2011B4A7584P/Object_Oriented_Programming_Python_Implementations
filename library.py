class Library:

    def __init__(self, list_of_books):
        self.available_books = list_of_books
        print('Welcome to Library')

    def display_available_books(self):
        print('Available Books :')
        for book in self.available_books:
            print(book)

    def issue_book(self, requested_book):
        if requested_book in self.available_books:
            print('Requested book has been issued')
            self.available_books.remove(requested_book)
        else:
            print('Sorry! The book is not available at the moment')

    def add_book(self, returned_book):
        self.available_books.append(returned_book)
        print('Thank you for returning the book!')


class Student:

    @staticmethod
    def request_book():
        return input()

    @staticmethod
    def return_book():
        return input()


if __name__ == '__main__':

    library = Library(['The Last Prophet', 'Manual of Warrior of Light',
                      'Man\'s Search for Meaning', 'The Last Lecture'])

    student = Student()

    while True:

        print('Press 1 to see list of available books')
        print('Press 2 to request for a book')
        print('Press 3 to return a book')
        print('Press 4 to exit')

        print('Please enter a number to continue :\n')

        service_input = int(input())

        if service_input == 1:
            library.display_available_books()
        elif service_input == 2:
            print('Please enter the name of the book you want to get issued')
            requested_book = student.request_book()
            library.issue_book(requested_book)
        elif service_input == 3:
            print('Please enter the name of the book you want to return')
            returned_book = student.return_book()
            library.add_book(returned_book)
        else:
            quit()