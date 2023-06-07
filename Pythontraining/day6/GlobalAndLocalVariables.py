
#global_var=20  #global variable(outside the function)

#def func():
#    local_val=10   #local variable(inside the function)
#    print(local_val)
#    print(global_var)


#local variable accesable only inside the function
#global variable accesable everywhere

#func()

# print(local_var)  #invalid bcoz local_val is local variable of func . not accesibale outside func

#print(global_var)   #valid bcoz global_var is global

##################################################

#using global variable in local variable and update value
xy=100  #global variable

#def cool():
#    global xy   #update 100--->200
#    xy=200   #local variable
#    print(xy)

#cool()     #200
#print(xy)  #200

##################################################
#x=100
#print(x)  #--->100
#def cool():
#    global x
#    x=500
#    print(x)

#cool()     #---->500
#print(x)   #---->500


##################################################

# We can create global variable inside the function with "global" key
def cool():
    global x
    x=100
    print(x)

cool()    #100
print(x)  #100