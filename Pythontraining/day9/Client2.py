#import sys
#sys.path.append("C:/Users/kantoor/pycharmProjects/Pythontraining/day9/package1")
#sys.path.append("C:/Users/kantoor/pycharmProjects/Pythontraining/day9/package1/package2")
#import module1
#import module2
#module1.display()
#module2.show()

#Approach2
import  sys
sys.path.append("C:/Users/kantoor/pycharmProjects/Pythontraining/day9/package1")
sys.path.append("C:/Users/kantoor/pycharmProjects/Pythontraining/day9/package1/package2")

from module1 import *
from module2 import *

display()
show()