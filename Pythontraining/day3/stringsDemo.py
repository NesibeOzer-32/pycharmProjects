#create string variable

#ways of creating string variable
s="welcome"
s='welcome'
s=str('welcome')
s=str("welcome")

#creating empty string variables
name=""
name=''
name=str()

# mutable-can change the value of the variable ,
# immutable-cannot change the value of the value

#string is inmutable

str1="welcome"
print(id(str1))

#1925495801200

str1=str1+ "to python"
print(id(str1))
print(str1)

#1502701360096

#if the value is changed after updation then its immutable


#ex: + and * with string

strx="welcome"
print(strx+"programming") #concatenation/joining
print(strx*3) #welcomewelcomewelcome

#ex:slicing
#starting index 0
#ending index
stra="welcome"
print(stra[1:3]) #el
print(stra[:6]) #welcom
print(stra[2:]) #lcome

print(stra[1:-1]) # - remove last  1 number -->elcom
print(stra[1:-2]) # - remove last  2 number -->elco

#ex: ord() and chr()
print(ord('A'))  #65 returns the ASCII code of the character
print(chr(65))   #A returns character represented by a ASCII number

#ex: max()
# min()
# len()

print(max("abc")) #c
print(min("abc")) #a
print(len("welcome")) #7


#ex: in , not in operators
s="welcome"
print("come" in s)  #true
print("lome" in s)  #false

print("come" not in s)  #false
print("lome" not in s)  #true

#ex: string comparison
print("tim"=="tie")  #false
print("free" != "freedon")#true
print("abc" > "abd")#false
print("right" >= "left")#true
print("teeth" < "tee")#false
print("yellow"< "fellow")#false
print("abc" > "")  #true

#ex testing strings true/false
k="welcome to python"

print(k.isalnum()) #false
print("welcome".isalpha()) #true
print("2012".isdigit())#true
print("first number".isidentifier())#false --> reserved keywords in python
print(k.islower())#true
print("WELCOME".isupper())#true
print(" ".isspace()) #true

#ex:searching for substring
m='welcome to python'

print(m.startswith("wel")) #true
print(m.endswith("hon"))#true
print(m.find("come")) #3 possition
print(m.find("become"))#-1 not found
print(m.count("o"))#3 returns number of occurences of substring the string

#converting String
t="String in PYTHON"
t1=t.capitalize() #String in python
print(t1)

t2=t.title()  #String In Python
print(t2)

t3=t.lower()  #string in python
print(t3)

t4=t.upper()  #STRING IN PYTHON
print(t4)

t5=t.swapcase() #sTRING IN python
print(t5)

t6=t.replace("in","on")  #Strong on PYTHON
print(t6)

#ex: Reverse a string
#method 1
#y="welcome"
#rev_str=""

#for i in y:
#    rev_str=i+rev_str
#print("reserved string is : ", rev_str)

#method2
y="welcome"
rev_str=y[::-1]
print(rev_str)