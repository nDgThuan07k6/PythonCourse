from abc import ABC, abstractmethod

class AbstractAnimal(ABC):

    # Using abstractmethod to force subclass to override or else error
    @abstractmethod
    def speak(self):
        pass

class Dog(AbstractAnimal):
    def speak(self):
        return 'Woof! Woof!'
    
dog = Dog()
print(dog.speak())