''' a program about animals '''

class Animal(object):
    def __init__(self):
        self.food = 'food'
        self.sound = 'sound'


    def talk(self):
        print '%s I like %s' % (self.sound,self.food)


class Cat(Animal):
    def __init__(self):
        self.sound = 'meow'
        self.food = 'mice'
    


if __name__ == '__main__':
    cat = Cat()
    cat.talk()

