import sys
sys.path.append("C:/Users/kantoor/pycharmProjects/Pythontraining/day9/packageA")
sys.path.append("C:/Users/kantoor/pycharmProjects/Pythontraining/day9/packageB")

import emp
empobj=emp.Employee(101,"John",500000)
empobj.displayemp()

import stu
stuobj=stu.Student(1121,"Scott",'B')
stuobj.displaystu()

#Approach2
from emp import Employee
empobj=Employee(101,"John",500000)
empobj.displayemp()

from stu import Student
stuobj=Student(1121,"Scott",'B')
stuobj.displaystu()