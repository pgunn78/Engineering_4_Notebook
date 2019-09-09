#Writtin by Zane&Paxton

a = float(input('1st num: '))
b = float(input('2nd num: '))

def doMath(a,b,c):
    if (c == 1):
        result = a+b
    elif (c == 2):
        result = a-b
    elif (c == 3):
        result = a*b
    elif (c == 4):
        result = round(a/b,2)
    elif (c == 5):
        result = a%b
    return str(result)

print("sum:\t\t" + doMath(a,b,1))
print("Difference:\t\t" + doMath(a,b,2))
print("Product:\t\t" + doMath(a,b,3))
print("Quotient:\t\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))