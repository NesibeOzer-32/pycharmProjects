#creating set
#set is mutable

#myset={"apple","banana","cherry"}
#print(myset) #{'apple', 'banana', 'cherry'}

##################################################

#Accessing items from set
#myset={"apple","banana","cherry"}
#for i in myset:
#    print(i)

##################################################

#value exist in set or not
#myset={"apple","banana","cherry"}

#print("banana" in myset)  #true
#print("banana2" in myset)  #false

##################################################

#adding items to set
#add() -add single item
#update() - add multiple items

#myset={"apple","banana","cherry"}
#print(myset)

#myset.add("orange")
#print(myset) #{'orange', 'apple', 'cherry', 'banana'} unorderd

#myset.update(["mango","grapes"])
#print(myset)

##################################################

#find number of items in a set
#myset={"apple","banana","cherry"}
#print(len(myset)) #3

##################################################

#remove item from the set
#myset={"apple","banana","cherry"}
#myset.remove("apple")
#print(myset) #---> {'banana', 'cherry'}
#myset.remove("xyz") #KeyError: 'xyz ***sette olmayan birsey yazilinca remove hata verir

#myset.discard("banana")
#print(myset)  #{'cherry', 'apple'}
#myset.discard("xyz")
#print(myset)  #{'apple', 'cherry'} discard ile sette olmayan birsey silinsin istediginde hata vermez

##################################################

#clear all items from the set
#myset={"apple","banana","cherry"}
#myset.clear()
#print(myset)  #-->set()

#completly delete the set variable
#del myset
#print(myset) #NameError: name 'myset' is not defined

##################################################

#joining 2 set -union()
#set1={"a","b","c"}
#set2={1,2,3}
#set3=set1.union(set2)
#print(set3)  #{1, 2, 'b', 3, 'a', 'c'}

#update
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)  #{1, 2, 3, 'b', 'c', 'a'}

