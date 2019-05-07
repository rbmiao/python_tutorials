#!/usr/bin/python
# -*- coding: UTF-8 -*-

 
class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee is {}".format(Employee.empCount))
 
   def displayEmployee(self):
      print("Name : {},  Salary: {} ".format(self.name, self.salary))

   def displayEmployeeExtra(self):
      print("Name : {},  Salary: {}, age is {}".format(self.name, self.salary, self.age))

e1 = Employee('daniel', 1000)
e2 = Employee('miao', 2000)

e1.displayEmployee()
e2.displayEmployee()

e1.displayCount()
e2.displayCount()

print(e1.name)
print(e2.salary)

e1.age=23
e2.age=45

e1.displayEmployeeExtra()
e2.displayEmployeeExtra()

print(e1.__dict__)
print(e1.name)
print(e1.__doc__)
print(e1.__module__)

print(id(e1), id(e2))

del e1,e2
