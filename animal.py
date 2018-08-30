class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health
    #Decrease health by 1 with every use of walk()
    def walk(self):
        self.health -= 1
        return self
    #Decrease health by 5 with every use of run()
    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health
        print self.name

# Create Dog class that inherits all of the Animal class's methods
class Dog(Animal):
    def __init__(self,name,health):
        super(Dog, self).__init__(name,health)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

# Create Dog class that inherits all of the Animal class's methods
class Dragon(Animal):
    def __init__(self,name,health):
        super(Dragon,self).__init__(name,health)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon,self).display_health()
        print 'I am a Dragon'

class FakeAnimal(Animal):
    def fake(self):
        print 'I am a fake animal'
        

# Task 1

# animal1 = Animal('Snuggles', 100)
# animal1.display_health()
# animal1.walk().walk().walk().run().run().display_health()

# Task 2

dog1 = Dog('Snuggles',100)
# dog1.walk().walk().walk().run().run().pet().display_health()

# # Task 3 (made it up myself to test Dragon class as there were no instructions to do so)

# dragon1 = Dragon('Scaly', 100)
# dragon1.fly().display_health()

# Task 4

fake = FakeAnimal('Fakey',0)
# fake.fly().display_health()
# fake.pet().display_health()
# fake.display_health()
dog1.fly()


# class Dog(Animal):

# class Dragon(Animal):