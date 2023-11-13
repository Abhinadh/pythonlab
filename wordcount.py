n=input("enter a string")
s=int(input("enter a number"))
f=list(n.split(" "))
d=[]
for i in f:
    co=len(i)
    if co >s:
        d.append(i)
        
print("anew string",d)
