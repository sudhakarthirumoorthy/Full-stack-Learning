class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  # private
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Age is Setted")

people = Person("sudhakar",24)
print(people.get_age())
people.set_age(23)
print(people.get_age())