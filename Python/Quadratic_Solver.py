#Written By Zane&Paxton
import math
print("Quadratic Solver\nEnter the coefficients for ax^2 +bx +c = 0")

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

def findRoots (a,b,c):
    Des = (b**2) - (4*a*c)
    roots = []
    if (Des < 0):
        print("no real roots")
    elif (Des >= 0):
        root1 = (-b+math.sqrt(Des))/(2*a)
        root2 = (-b-math.sqrt(Des))/(2*a)
    roots.append(root1)
    roots.append(root2)
    return roots

Quadratic = findRoots(a,b,c)
print("Here are your roots:")
for x in Quadratic:
    print(x)