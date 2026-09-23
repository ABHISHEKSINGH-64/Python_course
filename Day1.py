# Arithmetic Operators

a = 10
b = 10

print(a+b)
print(a-b)
print(a*b)
print(a % b)
print(a / b)

# Logical Operators
a = True
b = False

print(a and b)
print(a or b)
print(not b)


# Conditional Operators
a = 10 
b = 20

print( a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

# CIRCLE
r = 5
Area = (22/7) * r * r
print("Area of circle: " , Area)
circumfernce = 2*(22/7) * r
print("circumfernce of circle: ", circumfernce)

#  CONE
r = 5
l = 10
TotalArea = (22/7) * r * (r + l)
print("TotalArea of cone: " , TotalArea)
Volume = (1/3) * (22/7) * r * r * l
print("Volume of cone: " , Volume)


# TRIANGLE
a,b,c = 3,4,5
s = (a + b + c) / 2
Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of triangle: " , Area)

# CYLINDER
r = 5
h = 10
TotalArea = 2 * (22/7) * r * (r + h)
print("TotalArea of cylinder: " , TotalArea)

Volume = (22/7) * r * r * h
print("Volume of cylinder: " , Volume)

# SIMPLE INTREST (SI)
p = 100000
r = 5
t = 10

SI = (p * r * t) / 100
A = p + SI
t = (10 / 12)

print("Simple Interest:", SI)
print("Time:", t)

# COMPOUND INTREST (CI)
P = 100000
R = 5
T = 10

A = P * (pow((1 + R / 100), T))
CI = A - P
print("Compound Interest:", CI)
