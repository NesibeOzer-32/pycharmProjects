#how to create class

#class MyClass:
#    def myfun(self):
#        pass  #nun empty
#    def display(self,name):
#       print(name)

#mc1=MyClass()
#mc1.myfun()
#mc1.display("john")  #john
#instance method
#------------------------------------------------------------------------------------------#

#class MyClass:#self'lerin renkleri farkli
#    def m1(self):#burda self sinif ismini temsil ediyor
#        print("this is instance method...")
#    @staticmethod
 #   def m2(self,num):#burda self parameterlardan birini temsil ediyor
  #      print(self,num)

#mc= MyClass()
#mc.m1()
#mc.m2(100,200)

#MyClass.m2(10,20) #10,20 @here calling static method directly using class not through obj

#------------------------------------------------------------------------------------------#

#class Myclass:  # if we want to use class variables in method we have to use self keyword

 #   a,b=10,20   #class variables
 #   def add(self):
 #       print(self.a+self.b)
 #   def mul(self):
 #       print(self.a*self.b)

#mc=Myclass()
#mc.add()
#mc.mul()


#------------------------------------------------------------------------------------------#

#i,j=15,25                 #global variables

#class MyClass:
#    a,b=10,20             # class variables
#    def add(self,x,y):
#        print(x+y)             #x,y are local variable
#        print(self.a+self.b)   # a,b  class variables
#        print(i+j)             #i,j  global variables

#mc=MyClass()
#mc.add(10,70)

#------------------------------------------------------------------------------------------#

#a,b=15,25                 #global variables

#class MyClass:
 #   a,b=10,20             # class variables
  #  def add(self,a,b):
   #     print(a+b)  #local variables
    #    print(self.a+self.b)  #class variables
    #   print(globals()['a']+globals()['b'])  #global variables
      #  print(a+b)  #how to acsess global variables they have same name with local---> with globals() key


#mc=MyClass()
#mc.add(10,70)


#------------------------------------------------------------------------------------------#

#one class can have multiple obj
#class Myclass:
#    def display(self,name):
#        print("this is display method......")
#        print(name)

#obj1=Myclass()
#obj1.display("john")
#obj2=Myclass()
#obj2.display("scott")

#------------------------------------------------------------------------------------------#

#constructor example
#class Myclass:
#    def __init__(self):
#        print("this is constructor")
#    def m1(self):
#        print("Hello....")
#    def m2(self,x,y):
#        return(x+y)

#mc=Myclass()        #INVOKE constructor automatically--> output :this is constructor
#mc.m1()             #method we have call explicitely by using obj
#res=mc.m2(10,20)
#print(res)

#------------------------------------------------------------------------------------------#

#class MyClass:
#    name="john"
#    def __init__(self,name):  #constructor expecting one argument
#        print(name)
#        print(self.name)

#mc=MyClass("David") #passing parameter to the constructor

#------------------------------------------------------------------------------------------#
#req:emp
#constr: empl_id, empl_name, salary
#display(): print  empl_id, empl_name, salary

#class Emp:

#    def __init__(self,empl_id, empl_name, salary): #nothing return
#        self.empl_id=empl_id # with self keyword belongs to the class
#        self.empl_name=empl_name
#        self.salary=salary
#    def display(self):
#        print(self.empl_id,self.empl_name,self.salary)





#e1=Emp(101,"John",500000)
#e1.display()

#e2=Emp(102,"Scott",700000)
#e2.display()
#========================================================
#if all values string use below
#class Emp:

#    def __init__(self, empl_id, empl_name, salary):  # nothing return
#        self.empl_id = empl_id  # with self keyword belongs to the class
#        self.empl_name = empl_name
#        self.salary = salary

#    def __str__(self):  #string
#        return (self.empl_name,self.salary)


#e1 = Emp(101, "JOHN", 500000)  #TypeError: __str__ returned non-string (type tuple)
#print(e1)

