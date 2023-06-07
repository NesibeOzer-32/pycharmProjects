#break continue

#break if i==5--> 1,2,3,4,5
#for i in range(1,10):
#    if i ==5:
 #       break
  #  print(i)  #
#print("program exited!!!")


#skip 5 and continue --> 1,2,3,4,6,7,8,9
#for i in range(1,10):
#    if i ==5:
#        continue
 #   print(i)  #
#print("program continue!!!")

#skip 3, 5, 7 and continue --> 1,2,4,6,8,9
for i in range(1,10):
    if i==3 or i ==5 or i==7:
        continue
    print(i)  #
print("program continue!!!")