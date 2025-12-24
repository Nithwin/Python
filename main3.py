# Class and Objects

# class Parent:
#     def __init__(self, name):
#         self.name = name
#         print('Parent')
#     def eat(self):
#         print('Eating')
# class Child:
#     def __init__(self, age):
#         self.age = age
#         print('Child')
#     def eat(self):
#         print('Sleeping')

# class GrandChild(Child, Parent):
#     def __init__(self, name, age, year):
#         super().__init__(age)
#         self.year = year

# g2 = GrandChild("g1", 12, 2022)
# g2.eat()
# g2.eat()

# c1 = Child("c1", 12)
# p1 = Parent("name")
# print(p1.name)

# print(c1.age)
# print(c1.name)

# class Student:
#     def __init__(self, name):
#         self.name = name
#     def PrintName(self):
#         print(self.name)

# s1 = Student('Abc')
# s1.PrintName()
# Student('Abc').PrintName()


# class Student:
#     _college = 'nec'
#     def __init__(self, name):
#         self.name = name
#     @classmethod
#     def updateCollege(cls,college):
#         cls._college = college
    
#     def printCollege(cls):
#         print(cls._college)

# s1 = Student("s1")
# s2 = Student("s1")
# Student.updateCollege('nct')
# s1.printCollege()
# s2.printCollege()


# class Student:
#     def __init__(self, name, reg_no="not assigned"):
#         self._name = name
#         self._reg_no = reg_no
#     # def details(self):
#     #     print(self.reg_no)
#     #     print(self.name)
#     def setName(self, name):
#         self._name = name
#     def getName(self):
#         return self._name
#     def setRegno(self, reg_no):
#         self._reg_no = reg_no
#     def getRegno(self):
#         return self._reg_no


# student1 = Student("Abc", 1234)
# student1 = Student("Xyz")
# student2 = Student("Xyz")
# student1.details()
# student2.details()
# print(student2.getName())
# student2.setName('Python')
# print(student2.getName())
#print(main)
#CamelCase
#ClassRoom

# class Vehicles:
#     pass

# class Cars:
#     pass

# class Bikes:
#     pass




#print([age for i in range(0, int(input())) if (age:=int(input())) >= 18])

# n = int(input())
# c = 0
# for i in range(0, n):
#     if (age := int(input())) >= 18:
#             c += age
# print(c)