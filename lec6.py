class Animal:
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