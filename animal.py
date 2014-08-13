''' a program about animals '''

from subprocess import check_output

class Animal(object):
    def __init__(self):
        self.food = 'food'
        self.sound = 'sound'
        self.name = 'animal'

    def talk(self):
        message = 'I am a %s. %s. I like %s.' % (self.name, self.sound, self.food)
        print message
        check_output(['say', message])


class Cat(Animal):
    def __init__(self):
        self.sound = 'meow'
        self.food = 'mice'
        self.name = 'Cat'

class Dog(Animal):
    def __init__(self):
        self.sound = 'woof'
        self.food = 'dead animals'
        self.name = 'Dog'

class Goat(Animal):
    def __init__(self):
        self.sound = 'maaah'
        self.food = 'alfalfa'
        self.name = 'Goat'

class Horse(Animal):
    def __init__(self):
        self.sound = 'neigh'
        self.food = 'hay'
        self.name = 'Horse'


if __name__ == '__main__':
    cat = Cat()
    cat.talk()

    goat = Goat()
    goat.talk()

    dog = Dog()
    dog.talk()

    horse = Horse()
    horse.talk()



