#class A:
#    def m1(self):
#        print("this is m1 method from class A")
#class B(A):
#    def m2(self):
#        print("this is m2 method from class B")


#bobj=B()
#bobj.m1()  #this is m1 method from class A
#bobj.m2()  #this is m1 method from class A

#------------------------------------------------------------------------------------------#
#class A:
#    x,y=10,20
#    def m1(self):
#        print(self.x+self.y)

#class B(A): #A is parent of B
#    a,b=100,200
#    def m2(self):
#        print(self.a-self.b)

#bobj=B()
#bobj.m1()
#bobj.m2()

#------------------------------------------------------------------------------------------#
#multi level inheritance

#class A:  #A daki herseyi icerir
#    x,y=10,20
#    def m1(self):
#        print(self.x+self.y)


#class B(A):  #B ve A dai herseyi icerir
#    a, b = 200, 100

#    def m2(self):
#        print(self.a - self.b)

#class C(B):  #A,B VE C deki hersey icerir
#    i,j=5,2
#    def m3(self):
#        print(self.i*self.j)

#cobj=C()
#cobj.m1()
#cobj.m2()
#cobj.m3()

#------------------------------------------------------------------------------------------#
# Heirarchy  inheritance

#class A:  #A daki herseyi icerir
#    x,y=10,20
 #   def m1(self):
 #       print(self.x+self.y)


#class B(A):  #B ve A daki herseyi icerir
#    a, b = 200, 100

#    def m2(self):
#        print(self.a - self.b)

#class C(A):  #A VE C deki hersey icerir
#    i,j=5,2
#    def m3(self):
#        print(self.i*self.j)

#bobj=B()
#bobj.m1()
#bobj.m2()

#cobj=C()
#cobj.m1()
#cobj.m3()

#------------------------------------------------------------------------------------------#
# Multiple  inheritance

#class A:
#    x,y=10,20
#    def m1(self):
#        print(self.x+self.y)


#class B:
#    a, b = 200, 100

#    def m2(self):
#        print(self.a - self.b)

#class C(A,B):  #A,B ve C deki hersey icerir
#    i,j=5,2
#    def m3(self):
#        print(self.i*self.j)


#cobj=C()
#cobj.m1()
#cobj.m2()
#cobj.m3()

#------------------------------------------------------------------------------------------#
# Multiple  inheritance

#class A:

#    def m1(self):
#        print("This is m1 method from class A")


#class B(A):

#    def m1(self):
#        print("This is m1 method from class B")
#        super().m1()  #without super method when we run we can not see "This is m1 method from class A"

#bobj=B()
#bobj.m1()

#------------------------------------------------------------------------------------------#

class A:
    a,b=10,20

#class B(A):
#    i,j=100,200
#    def m(self,x,y):
#        print(x+y)  #Local variables
#        print(self.i+self.j)  #class variables
#        print(self.a+self.b)  #class variables

#bobj=B()
#bobj.m(1000,2000)

#------------------------------------------------------------------------------------------#
#overriding variables

#class Parent:
#    name="Scott"

#class Child(Parent):
#    name = "John"  #overriding the variable value

#cobj=Child()
#print(cobj.name)


#------------------------------------------------------------------------------------------#
#override the methods

#class Bank():
#    def rateOfInterest(self):
#        return 0
#class XBank(Bank):
#    def rateOfInterest(self):
#        return 10
#class YBank(Bank):
#    def rateOfInterest(self):
#        return 12

#objx=XBank()
#print(objx.rateOfInterest())

#objy=YBank()
#print(objy.rateOfInterest())

#------------------------------------------------------------------------------------------#

#class Human:
#    def sayHello(self,name=None):
#        if name is not None:
#            print("Hello " + name)
#        else:
 #           print("Hello")

#h=Human()
#h.sayHello("Scott")
#h.sayHello()

#------------------------------------------------------------------------------------------#

class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

calobj=Calculation()
calobj.add()            #0
calobj.add(10,20)       #
calobj.add(100,200,300)
