# datascience
#data types in python 
#  mutable  list,set,array....
#  immutable  tuple,dict,....

 # list
list=[1,2,3,4,5] 
print(list)
# list type()
list1=[1,2,3,4,5]
print(type(list1))
# list len()
list2=[1,2,3,4,5]
print(len(list2))

# list change
list3=["blue","green","red","blue"]
list3[2]="orange"
print(list3)
# acssing 
list4=["hema","liku","nalu","giri","hari"]
print(list4[1])
print(list4[2])
print(list4[2:4])
print(list4[-1]) 
# check it exits
list5=[1,2,3,4]
if 2 in list5:
 print("yes its there" )

 list6=["hema","latha","likku","nalu"]
 if "nalu" in list6:
  print(list6)
# change 
list7=["blue","green","red","blue"]
list7[2:3]=["orange"]
print(list7)
# insert
list8=["blue","green","red","blue"]
list8.insert(3,"orange")
print(list8)
# append
list9=["blue","green","red","blue"]
list9.append("orange")
print(list9)

list9=["blue","green","red","blue"]
list9.append(["orange","skyblue"])
print(list9)

list10=[1,2,3,4,5] 
list10.append([6,7])
print(list10)

#  extend
list11=["blue","green","red","blue"]
list11.extend(["orange","skyblue"])
print(list11)

list12=[1,2,3,4,5] 
list12.extend([6,7,8,9])
print(list12)
# remove
list13=["blue","green","red","blue"]
list13.remove("red")
print(list13)

list14=["blue","green","red","blue"]
list14.pop(1)
print(list14)

list14=["blue","green","red","blue"]
list14.pop()
print(list14)

# loops
list15=[1,2,3,4]
for x in list15:
 print(x)

list16=[1,2,3,4]
for x in list16:
 print(x ,end=' , ')

# lenth

list17=[1,2,3,4]
for x in range(len(list17)):
 print(x)

  # sorted
list18=[2,3,41,6,5,7,0]
list18.sort()
print(list18)

# sorted reverse
list19=[7,8,4,56,7,]
list19.sort(reverse=True)
print(list19)

# copy
list20=[1,2,3,4,5]
list=list20.copy()
print(list)

list20=[1,2,3,4,5]
list=(len(list20))
print(list)

list21=["banana","apple","grapes"]
list22=["orange","kewi"]
list=list21+list22
print(list)


