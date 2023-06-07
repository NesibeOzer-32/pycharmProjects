

#def func(i,j):
#    print(i,j)

#func(10,20)      #possitional arguments
#func(j=20,i=10)   #keyword arguments


#default values assigned to possitional arguments
#def func(i,j=10):
#    print(i,j)
#func(100,200)
#func(100)

#keyword arguments
#def greetings(name,greetmsg):
#    print(greetmsg+"    "+name)

#greetings(name='John',greetmsg='Hello')
#greetings(greetmsg='Hello',name='John')

################

#def my_fun(a,b,c):
#    print(a,b,c)

#my_fun(10,20,30)    #possitional parameters
#my_fun(a=10,b=20,c=30)  #Keywoord arguments
#my_fun(b=20,c=30,a=10)  #Keywoord arguments

#my_fun(10,20,c=30)
#my_fun(10,b=20,c=30)
#my_fun(10,b=20,30) #SyntaxError: positional  argument follows keyword argument
# -->this is wrong as possitional argument must appear before any keyword argument
#--> positional arg always before keyword argument
#my_fun(10,30,b=20)  #this is having logical error a

################

#def largest(a,b):
#    if a>b:
#        return a,b
#    else:
#        return b,a

#print(largest(9,7))
#print(largest(90,75))
#print(largest(19,700))

#res=largest(10,20)
#print(res)

#print(type(res))  #----><class 'tuple'>