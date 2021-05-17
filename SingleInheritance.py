class Apple:
    contact_website = 'https://www.apple.com'


class Macbook(Apple):

    def __init__(self):
        print('Welcome,this is a Macbook')
        print('For more information, log on to {}'.format(self.contact_website))


if __name__ == '__main__':
    macbook = Macbook()
