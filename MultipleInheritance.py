class OperatingSystem:
    multitasking = True
    name = 'MacOS'


class Apple:
    contact_website = 'https://www.apple.com'
    name = 'Apple'


class Macbook(OperatingSystem, Apple):
    def __init__(self):
        print('This is a multitasking {} system!'.format(self.name))
        print('Obviously, it is an {} product'.format(Apple.name))
        print('For more information, log on to {}'.format(self.contact_website))


if __name__ == '__main__':
    macbook = Macbook()
