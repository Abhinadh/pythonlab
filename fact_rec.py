def fact(n):
    """factorial of a number using recursion"""
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number"))

if n<0:
    print("factorial not possible")
print("factrial of %d is %d"%(n,fact(n)))
