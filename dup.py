n=input("enter the list ")
n=list(map(int,n.split(",")))
d=[]
d=[d.append(i) for i in n if (i not in d)]
#for i in n:
    #if(i not in d):
        #d.append(i)
print(d)
