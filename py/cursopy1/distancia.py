import math
x=float(input("primeiro dado x ")) 
y=float(input("primeiro dado y "))
x1=float(input("primeiro dado x1 ")) 
x2=float(input("primeiro dado x2 "))

plano = math.sqrt(((x - y) ** 2) + ((x1 - x2)**2)) 

if plano >= 10:
    print("longe")
else:
    print("perto")