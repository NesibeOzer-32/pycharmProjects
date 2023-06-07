#if  if...else

#example1 : Print a person is eligible for vote or not
#age>=18

age=15
if age>=18:
    print("Eligible for vote")
else:
    print("NOT Eligible for vote")

#Example2

if True:
    print("True condition")
else:
    print("false condition")

#Example3

if 1:
    print("one")
else:
    print("Not one")

#Exapmle: find a number is even/odd num%2=0 even

num=10

if num%2==0:
    print("Given number is Even")
else:
    print("Given number is odd")

#TERNARY OPERATO: if else in single line
num1=11
print("Even number") if num1%2==0 else print("odd number")

#example if else - multiple statments in Single Line
a=19
{print("hello"),print("python")} if a>=10 else {print("hi"),print("java")}

#example: multiple condition using elif

weeknu=5

if weeknu==1:
    print("sunday")
elif weeknu==2:
    print("monday")
elif weeknu==3:
    print("tuesday")
elif weeknu==4:
    print("wednesday")
elif weeknu==5:
    print("thursday")
elif weeknu==6:
    print("friday")
elif weeknu==7:
    print("saturday")
else:
    print("Invalid week number")

