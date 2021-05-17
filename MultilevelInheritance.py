class MusicalInstruments:
    keys = 12


class StringInstruments(MusicalInstruments):
    material = 'Tonewood'


class Guitar(StringInstruments):
    def __init__(self,color):
        self.color = color
        print('It\'s a {} guitar made of {} and has {} keys'.format(self.color,self.material,self.keys))


if __name__ == '__main__':
    guitar = Guitar('brown')