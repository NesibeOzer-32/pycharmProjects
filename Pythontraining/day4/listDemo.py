#mylist1=[10,20,30,40,50]
#mylist2=["apple","banana","cherry"]
#mylist3=["apple",10,"banana",20]
#mylist=list()

#print(mylist)
#print(mylist1)
#print(mylist2)
#print(mylist3)

#ex: accessing items from the list
#mylist=["apple","banana","cherry"]  #index strarts from 0
#-1 last element - ile sondan basliyor

#print(mylist[0])
#print(mylist[2])
#print(mylist[-1])
#print(mylist[-2])


#ex range of indexes
#mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
#print(mylist[2:5])   #['cherry', 'orange', 'kiwi']

#print(mylist[-4:-1])  #['orange', 'kiwi', 'melon']

#ex: change item value
#mylist=["apple","banana","cherry"]
#print(mylist)   #['orange', 'kiwi', 'melon']
#mylist[0]="orange"
#print(mylist)  #['orange', 'banana', 'cherry']

#ex: how to read the list items using loop
#mylist=["apple","banana","cherry"]

#for i in mylist:
#    print(i)

#ex: check if the item is exist in the list or not
#mylist=["apple","banana","cherry"]
#if "apple" in mylist:
#    print("yes, apple is present")
#else:
#    print("No, apple is not present")

#ex:list length(counting number of items in a list)
#mylist=["apple","banana","cherry"]
#print(len(mylist))

#############33333#3#33#############33###33###33333#33####333#

#ex: add items
#append()
#insert()
#mylist=["apple","banana","cherry"]
#mylist.append("orange") #['apple', , 'banana', 'cherry', 'orange']--> adds by default at the end of the list
#mylist.insert(1,"orange") #--->add item some where in the middle of the list based on the index
#print(mylist) #['apple', 'orange', 'banana', 'cherry']

#############33333#3#33#############33###33###33333#33####333#
#remove item from the list

#pop()  --->method function
#mylist=["apple","banana","cherry"]
#mylist.pop(0) #specify the index number
#print(mylist)  ----->

#del  ---> keyword
#del mylist[1]  #here del command removes single item based on the index
#print(mylist)  ----->['banana']

#clear ---> function
#mylist=["apple","banana","cherry"]
#mylist.clear()  #remove all items
#print(mylist)  # -->[]

#############33333#3#33#############33###33###33333#33####333#

#copy list
#mylist1=["apple","banana","cherry"]
#mylist2=list(mylist1)
#print(mylist1) #['apple', 'banana', 'cherry']
#print(mylist2) #['apple', 'banana', 'cherry']

#mylist2=mylist1.copy()
#print(mylist1) #['apple', 'banana', 'cherry']
#print(mylist2) #['apple', 'banana', 'cherry']

#############33333#3#33#############33###33###33333#33####333#

#combine/join lists
#using = operators
#list1=["a","b","c"]
#list2=[1,2,3]
#list3=list1+list2
#print(list3)

#using loop statement
#list1=["a","b","c"]
#list2=[1,2,3]

#for i in list2:
#    list1.append(i)
#print(list1)    #['a', 'b', 'c', 1, 2, 3]

#using extend()
#list1=["a","b","c"]
#list2=[1,2,3]
#list1.extend(list2)
#print(list1) #['a', 'b', 'c', 1, 2, 3]

##############################################################

list1=(10,20,30)
list2=('a','b','c')

if list1==list2:
    print("lists are equal")
else:
    print("lists are not equal")