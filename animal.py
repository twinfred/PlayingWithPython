class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print str(self.name) + "'s health is currently at " + str(self.health)
        return self

animal1 = Animal("Max")
animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health += 50
    def pet(self):
        self.health += 5
        return self

dog1 = Dog("Peter")
dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        self.health += 70
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I'm a Dragon"
        return self

dragon1 = Dragon("Trevor")
dragon1.walk().walk().run().fly().fly().display_health()