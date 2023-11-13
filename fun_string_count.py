def string(n):
    """count the number of string"""
    count=0
    for i in n.split():
        if(len(i)>1 and i[0]==i[-1]):
            count+=1
    return count
n=input("enter some string")
print(string(n))
    
