#name="john"
#age=30
#sal=5000.50

#Aproach 1
name,age,sal="john",30,5000.50

print(name,age,sal)

#Approach2
print("Name is: ", name)
print("Age is: ", age)
print("Sal is: ", sal)


#Aproach3
print("Name is:%s Age is:%d Salary is:%g" %(name,age,sal))

#Aproach4
#   {}
print("Name is:{} Age is:{} Salary is:{}" .format(name,age,sal))
#order is important
print("Name is:%s Age is:%d Salary is:%g" %(age,name,sal)) #wrong order be careful
