class PreciousStone:
    count = 0
    stone_collection = []

    def __init__(self, name):

        self.name = name
        if PreciousStone.count < 5:
            PreciousStone.stone_collection.append(self)

        PreciousStone.count = PreciousStone.count + 1

        if PreciousStone.count > 5:
            del PreciousStone.stone_collection[0]
            PreciousStone.stone_collection.append(self)

    @staticmethod
    def display_stone_collection():
        for stone in PreciousStone.stone_collection:
            print(stone.name, end='\n')
        print()


if __name__ == '__main__':
    stone_1 = PreciousStone('Emerald')
    stone_2 = PreciousStone('Ruby')
    stone_3 = PreciousStone('Sapphire')
    stone_4 = PreciousStone('Topaz')
    stone_5 = PreciousStone('Amber')
    PreciousStone.display_stone_collection()
    stone_6 = PreciousStone('Phoenix')
    PreciousStone.display_stone_collection()
