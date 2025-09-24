# numbers are divided into 3 types
# 1) int ,2) float , 3) complex 

#int
x=1764
y=-2346
z=776666666666666666
print(x)
print(y)
print(z)


# float

x=1.233
y=2.e4
z=-3.4777E34
print(x)
print(y)
print(z)


# complex

x=3+2j
y=3-2J
s=2e3
print(x)
print(y)
print(s)

# changing into to float

x=1
z=1.2344
a=2+2j

c=float(x)
d=int(z)
e=complex(a)

print(c)
print(d)
print(e)

# random 

import random

print("Random float (0.0 to 1.0):", random.random())

print("randam int (1 to 5):",random.randint(1,10))
print("random float (5,10):",random.uniform(5,10))

numbers=[1,3,2,4,5]
print("random choise list:",random.choice(numbers))