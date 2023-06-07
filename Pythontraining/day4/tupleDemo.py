#creating tuple
#tuple is immutable
#if its immutable below things are not possible
#we can not modify existing value
#we can not append new value
#we can not insert a new value
#we can not remove a value

##############################################################

#mytuple=("apple","banana", "cherry")
#print(mytuple)

##############################################################

#access tuple items
#mytuple=("apple","banana", "cherry")
#print(mytuple[1]) #banana here index starts from 0
#print(mytuple[-1]) #cherry

##############################################################

#range of indexes
#mytuple=("apple","banana", "cherry","orange","kiwi","melon","mango")
#print(mytuple[2:5])    #('cherry', 'orange', 'kiwi')
#print(mytuple[-4:-1])  #('orange', 'kiwi', 'melon')

##############################################################

#changing tuple items- by defaoult tuple does not allow you change values bcoz it is immutable
#but there is work around
#tuple--> list(modify) --> tuple

#mytuple=("apple","banana", "cherry")

#mylist=list(mytuple)
#mylist[0]="orange"

#mytuple=tuple(mylist)
#print(mytuple)

##############################################################

#reading tuple items using loop
#mytuple=("apple","banana", "cherry")
#for i in mytuple:
#    print(i)

##############################################################

#check if item exist (searching of item in tuple)
#mytuple=("apple", "banana", "cherry")

#if "banana" in mytuple:
#    print("yes, banana is present")
#else:
#    print("no, banana is not present")

##############################################################

#tuple length- counting items in a tuple
#mytuple=("apple", "banana", "cherry")
#print(len(mytuple))

##############################################################

#add items to tuple = not possible bcoz tuple is immutable - can not change values/items
#mytuple=("apple", "banana", "cherry")
#mytuple[0]="orange"
#print(mytuple) -->TypeError: 'tuple' object does not support item assignment

##############################################################

#copy tuple
#mytuple1=("apple", "banana", "cherry")
#mytuple2=mytuple1
#print(mytuple2) #('apple', 'banana', 'cherry')

##############################################################

#removing items from tuple - not possible bcoz tuple is immutable
#mytuple=("apple", "banana", "cherry")
#mytuple.remove("apple")  #AttributeError: 'tuple' object has no attribute 'remove'
#del mytuple #NameError: name 'mytuple' is not defined. Did you mean: 'tuple'?
#print(mytuple)

##############################################################

#join/combine tuple
#tuple1=(10,20,30)
#tuple2=('a','b','c')

#tuple3=tuple1+tuple2
#print(tuple3) #(10, 20, 30, 'a', 'b', 'c')

##############################################################

tuple1=(10,20,30)
tuple2=('a','b','c')

if tuple1==tuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")