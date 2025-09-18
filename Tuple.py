# tuple
tuple=(1,2,3,4,5)
print(tuple)

tuple1=(1,2,3,4,5,)
print(type(tuple1))

tuple=("blue","orange","black",)
print(type(tuple))

tuple=("blue","orange","black",)
print(tuple[1])

tuple=("blue","orange","black",)
print(tuple[1:])

# update here we convert tuple into list 
tuple=("blue","orange","black",)
x=list(tuple)
x[1]="kiwi"
print(x)

#add
tuple=("blue","orange","black",)
x=list(tuple)
x.append(("kiwi","grapes"))
print(x)

tuple=("blue","orange","black",)
x=list(tuple)
x.extend(("kiwi","grapes"))
print(x)

#unpack

colour = ("blue", "orange", "black")
(b, y, z) = colour
print(b)
print(y)
print(z)

#loop
tuple=[12,33,4,55,67]
for x in tuple:
    print(tuple)

tuple=[1,23,3,4,5]
for x in range(len(tuple)):
    print(tuple[x])
    
# joins
tuple=[1,2,3,4,5]
tuple1=[6,7,8,9,0]
tuple3=tuple+tuple1
print(tuple3)