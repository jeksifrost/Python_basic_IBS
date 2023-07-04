class Animal:

    num = 0

    def __init__(self) -> None: 
        Animal.num += 1

    @staticmethod
    def count_animal():
        return Animal.num

    def voice(self):
        pass

class Hamster(Animal):
    def voice(self):
        print('Hrum')

class Raven(Animal):
    def voice(self):
        print('Kurk')

class Deer(Animal):
    def voice(self):
        print('Aaaa')

hamster = Hamster()
raven = Raven()
deer = Deer()

hamster.voice()
raven.voice()
deer.voice()

print(Animal.count_animal())