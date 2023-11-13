n=input("enter elemts")
s=list(n.split(","))
d=[]
for i in s:
    if(i not in d):
        d.append(i)
printf("no duplication:",d)
        
        
               
