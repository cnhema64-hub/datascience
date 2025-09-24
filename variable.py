# variable

a="hema"
print(a)

variable="nalina"
print(variable)

# type
 
x="eshika"
print(type(x))

# more value multiple variables

x,y,z="orange","banana","grapes"
print(x)
print(y)
print(z) 

# one value to multi variable
x=y=z="eshika"
print(x)
print(y)
print(z)

# global variable


x = "leela"

def add():
    global x
    x = "swetha"
    print("leela loves", x)

add()
print("swetha loves", x)


# string

a="hema"
print(a)


a="hema"
print(type(a))

x="well come to ashoka women's engineering college"
print(x[13])

# len()
x="well come to ashoka women's engineering college"
print(len(x))

# slicing .......return a range of characters by using the slice
x="well come to ashoka women's engineering college"
print(x[3:10])

# remove space

x="      hi hemaa"
print(x.strip())

#replace

a="kavitha"
print(a.replace("k" ,"l"))

# spliting
a="hello, kalpana"
print(a.split(","))

# sting concatintion

a=10
b=20
c=a+b
print(c)

a="apple"
b="is sweet"
c=a+ " " +b
print(c)