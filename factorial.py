def fact(n):
    """factorial of number """
    fact=1
    for i in range(n,0,-1):
        fact*=i
    return fact
n=int(input("enter a number"))

if n<0:
    print("factorial not possible")
print("factrial of%d is %d"%(n,fact(n)))

    
