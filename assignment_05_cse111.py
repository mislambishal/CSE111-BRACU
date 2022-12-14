# -*- coding: utf-8 -*-
"""Assignment_05_CSE111

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EnKCORjpWARGUwEwzXqpHD24SJ4XbIMz

#1
"""

class Exam:
    def __init__(self,number):
        self.mark = number

    def __add__(self, other):
        total = self.mark + other.mark
        return Exam(total)

Q1 = Exam(int(input("Quiz 1 (out of 10): ")))
Q2 = Exam(int(input("Quiz 2 (out of 10): ")))
Lab = Exam(int(input("Lab (out of 30): ")))
Mid = Exam(int(input("Mid (out of 20): ")))
Final = Exam(int(input("Final (out of 30): ")))
total = Q1 + Q2 + Lab + Mid + Final
print("Total marks: {}".format(total.mark))

"""#2"""

class Teacher:
    def __init__(self,name,dept):
        self.__name = name
        self.__department = dept
        self.__courselist = []

    def addCourse(self,other):
        self.__courselist.append(other.course)

    def printDetail(self):
        print(f'====================================')
        print(f'Name: {self.__name}')
        print(f'Department: {self.__department}')
        print(f'List of courses')
        print(f'====================================')
        for i in self.__courselist:
            print(i)
        print(f'====================================')


class Course:
    def __init__(self,course):
        self.course = course



t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")                          
c1 = Course("CSE 110 Programming Language I")                           
c2 = Course("CSE 111 Programming Language-II")                           
c3 = Course("CSE 220 Data Structures")                           
c4 = Course("CSE 221 Algorithms")                           
c5 = Course("CCSE 230 Discrete Mathematics")                           
c6 = Course("CSE 310 Object Oriented Programming")                           
c7 = Course("CSE 320 Data Communications")                          
c8 = Course("CSE 340 Computer Architecture") 
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()

"""#3"""

class Team:
    def __init__(self,name = None):
        self.__name = name
        self.__player = []
    
    def setName(self,name):
        if self.__name == None:
            self.__name = name
    def addPlayer(self,other):
        self.__player.append(other.player)
    
    def printDetail(self):
        print(f'=====================')
        print(f'Name: {self.__name}')
        print(f'List of Players:')
        print(f'{self.__player}')
        print(f'=====================')

class Player:
    def __init__(self,player):
        self.player = player

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()

"""#4"""

class Color:
    def __init__(self,color):
        self.clr = color

    def __add__(self,other):
        main = self.clr + other.clr
        
        if main == 'redyellow' or main == 'yellowred':
            return Color('Orange')
        elif main == 'redblue' or main =='bluered':
            return Color('Violet')
        elif main == 'yellowblue' or main=='blueyellow':
            return Color('Green')

C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)

"""#5"""

import math


class Circle:
    def __init__(self, r):
        self.__radius = r

    def getRadius(self):
        return self.__radius
    def setRadius(self,rad):
        self.__radius=rad

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, other):
        b= Circle(self.__radius + other.__radius)
        return b


c1 = Circle(4)
print("First circle radius:", c1.getRadius())
print("First circle area:", c1.area())
c2 = Circle(5)
print("Second circle radius:", c2.getRadius())
print("Second circle area:", c2.area())
c3 = c1 + c2
print("Third circle radius:", c3.getRadius())
print("Third circle area:", c3.area())

"""#6"""

class Triangle:
    def __init__(self,base,height):
        self.__base = base
        self.__height = height
    def getBase(self):
        return self.__base
    def setBase(self, base):
        self.__base = base
    def getHeight(self):
        return self.__height
    def setHeight(self, height):
        self.__height = height

    def area(self):
        return 0.5*self.__base*self.__height

    def __sub__(self,other):
        italy = self.getBase()- other.getBase()
        france = self.getHeight()- other.getHeight()
        return Triangle(italy,france)

t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())
 
t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())
 
t3 = t1 - t2 
print("Third Triangle Base:" , t3.getBase())
print("Third Triangle Height:" , t3.getHeight())
print("Third Triangle area:" ,t3.area())

"""#7"""

class Dolls:
    def __init__(self, name,price):
        self.name = name
        self.price = price

    def detail(self):
        if self.price <=3000:
            return f'Doll: {self.name}\n Total Price: {self.price}'
        else:
            return f'Dolls: {self.name}\n Total Price: {self.price}'

    def __gt__(self,other):
        if self.price>other.price:
            return True
        else:
            return False

    def __add__(self,other):
        return Dolls((self.name+other.name),(self.price+other.price))


obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_2 = Dolls("Daffy Duck", 1800) 
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

"""#8"""

class Coordinates:
    def __init__(self,val1,val2):
        self.value1 = val1
        self.value2 = val2
    
    def detail(self):
        return (self.value1,self.value2)

    def __sub__(self,other):
        brazil = self.value1 - other.value1
        argentina = self.value2 - other.value2
        return Coordinates(brazil,argentina)
    def __mul__(self,other):
        france = self.value1*other.value1
        italy = self.value2*other.value2
        return Coordinates(france,italy)

    def __eq__(self,main):
        if self.value1 == main.value1:
            return ('The calculated coordinates are the same.')
        else:
            return('The calculated coordinates are NOT the same.')

p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))

p4 = p1 - p2 
print(p4.detail())

p5 = p1 * p2
print(p5.detail())

point_check = (p4 == p5)
print(point_check)