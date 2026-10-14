
# # class Employee:
# #     name = "Sudhakar"
# #     salary = 23000
  

# # emp1 = Employee()       
# # emp2 = Employee()
# # emp1.name = "sudhakkar"
# # emp2.name = "balu"
# # print(emp1.name)
# # print(emp2.name)


# class Employee:
#     def __init__(self,name,salary):
#          self.name = name
#          self.salary = salary

# emp1 = Employee("sudhakar", 25000)
# emp2 = Employee("siva", 90000)

# print(emp1.salary)
# print(emp2.name)
# print(emp1.name)
# print(emp2.salary)

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# student1 = Student("Arun", 22)
# student2 = Student("Dharun", 24)

# print(student1.name)
# print(student2.age)


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name} my age is {self.age}")
student1 = Student("Arun", 22)
student1.introduce()