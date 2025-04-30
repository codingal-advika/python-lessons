from abc import ABC , abstractmethod
class animal(ABC):
    @abstractmethod
    def action(self):
        print('This is an abstract method')

class cat(animal):
    def action(self):
        print('I can Meow!')
    
class dog(animal):
    def action(self):
        print('I can Bark!')

class rabbit(animal):
    def action(self):
        print('I can growl and purr and like carrots')

c = cat()
c.action()

d = dog()
d.action()

r = rabbit()
r.action()
