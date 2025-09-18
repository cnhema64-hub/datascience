#set
set={1,2,3}
print(set)

# type
a={1,2,3,4}
print(type(a))

# unorder
set={"hema","geetha","kavya",1,2,3}
print(set)

# len
set={1,2,3,4,5,6,7}
print(len(set))

#accessing
set={1,2,3,4,5,6,7}
for x in set:
    print(x)
print("yes is there")

set={1,2,3,4,5,6,7}
print(1 in set)

set={"banana","grapes","cherry"}
print("cherry" in set)

set={"banana","grapes","cherry"}
print("cherry" not in set)

# adding
set = {"apple", "banana", "cherry"}
set.add("orange")
print(set)

# remove
set={"apple","banana","kiwi","apple1"}
set.remove(("apple1"))
print(set)

# loops
set = {"apple", "banana", "cherry"}
for x in set:
 print(x)

 set = {"apple", "banana", "cherry"}
for x in set:
 print(len(x))

 # join

 set={"abc","def","ghi"}
 set1={"jkl","mno","pqr"}
 set3=set.union(set1)
 print(set)


set={1,2,3,4,5,6,7}
set1={8,7,6,5,4,3,2,1}
set3=set|set1
print(set3)