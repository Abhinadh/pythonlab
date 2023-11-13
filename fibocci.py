def febi(n):
    """fibonocci series of a number"""
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
n=int(input("enter number"))
print("%d is the %d fibanocci number "%(n,febi(n)))



    
