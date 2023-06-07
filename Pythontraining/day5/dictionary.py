#written with curly brackets
#thet have keys and values
#mutable
#unorderd

#creating dictionary  {value:"key"}
#mydic={101:"x", 102:"y",103:"z"}
#print(mydic)  #{101: 'x', 102: 'y', 103: 'z'}

####################################################################

#access items from dictionary
#mydic={
#    "brand":"Hyundai",
#    "model":"i10",
#    "year":"2021"
#}

#print(mydic["brand"])
#print(mydic["model"])

#using get() funtion

#print(mydic.get("brand"))

####################################################################

#Change the values in dictionary

#mydic={
#    "brand":"Hyundai",
#    "model":"i10",
#    "year":"2021"
#}

#print(mydic)
#mydic["year"]=2022
#print(mydic)

####################################################################

#reading items from dictionary using loop
#mydic={
#    "brand":"Hyundai",
#    "model":"i10",
#    "year":"2021"
#}

#for i in mydic:
#    print(i)  # prints only keys from dictionary--->(brand,model,year)

#for i in mydic:
#    print(mydic[i])  # prints only values from dictionary

#for i in mydic.values():
#    print(i)          # prints only values from dictionary

#for x,y in mydic.items():  #prints keys along with the value
#    print(x,y)
    #brand Hyundai
    #model i10
    #year 2021

####################################################################

#check key is exist in dictionary or not

#mydic={
#    "brand":"Hyundai",
#    "model":"i10",
#    "year":2020
#}

#way1
#if "model" in mydic:
#    print("exist")
#else:
#    print("not exist")

#way3
#print("model" in mydic)

####################################################################

#find number of items in dictionary

#mydic={
#    "brand":"Hyundai",
#    "model":"i10",
#    "year":2020
#}

#print(len(mydic))  #3 pair


####################################################################

#adding items to dictionary

#mydic={
#    "brand":"Hyundai",
#    "model":"i10",
#    "year":2020
#}

#mydic["color"]="red"
#print(mydic)  #{'brand': 'Hyundai', 'model': 'i10', 'year': 2020, 'color': 'red'}

#####################################################################

#remove items from dictionary
#mydic={
#    "brand":"Hyundai",
#    "model":"i10",
#    "year":2020
#}
#print(mydic)          #{'brand': 'Hyundai', 'model': 'i10', 'year': 2020}
#mydic.pop("year")
#print(mydic)          #{'brand': 'Hyundai', 'model': 'i10'}

#del mydic["model"]
#print(mydic)          #{'brand': 'Hyundai'}

#del mydic             #delete complitely the dictioanary
#print(mydic)          #NameError: name 'mydic' is not defined

#mydic={
#    "brand":"Hyundai",
#    "model":"i10",
#    "year":2020
#}
#print(mydic)  #{'brand': 'Hyundai', 'model': 'i10', 'year': 2020}
#mydic.clear()
#print(mydic)  #{}


#####################################################################
#copying dictionary

#mydic1={
#    "brand":"Hyundai",
#    "model":"i10",
#    "year":2020
#}
#without using copy()
#mydic2=mydic1
#print(mydic1)   #{'brand': 'Hyundai', 'model': 'i10', 'year': 2020}
#print(mydic2)   #{'brand': 'Hyundai', 'model': 'i10', 'year': 2020}

#using copy
#mydic2=mydic1.copy()
#print(mydic2)
