import math
def perfct(n):
    sr=int(math.sqrt(n))
    return (sr*sr==n)
s=int(input("enter the limit"))
l=[]
for i in range(999,s):
    if (not i%2 and perfct(i)):
        l.append(i)
    
print("list is",l)        
