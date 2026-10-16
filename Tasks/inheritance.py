
class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type


class Lion(Animal):
    def zoo(self):
        print(f"{self.name} is a {self.animal_type}")


class Snake(Animal):
    def zoo(self):
        print(f"{self.name} is a {self.animal_type}")


class Elephant(Animal):
    def zoo(self):
        print(f"{self.name} is a {self.animal_type}")


# Create objects
a1 = Lion("Simba", "Lion")
a2 = Snake("Cobra", "Snake")
a3 = Elephant("Dumbo", "Elephant")

# Call methods
a1.zoo()
a2.zoo()
a3.zoo()
